from django.shortcuts import render
from redis import Redis
from django.core.files.storage import FileSystemStorage
import csv
from datetime import datetime

from library.DataWallLoader import DataWallLoader

def importer(request):

    error = False
    message = None
    datasetType = 'wr'
    datasetDate = datetime.today().strftime('%m/%d/%Y')

    if request.method == 'POST':
        datasetType = request.POST['dataset-type']
        datasetDate = request.POST['dataset-date']

        try:
            datasetDateObj = datetime.strptime(datasetDate, '%m/%d/%Y')
        except ValueError:
            return render(request, 'import.html', {'message': 'Please choose a date.', 'error': 'true', 'tab': datasetType, 'date': datasetDate})

        if 'dataset-file' not in request.FILES:
            return render(request, 'import.html', {'message': 'Please choose a file.', 'error': 'true', 'tab': datasetType, 'date': datasetDate})

        datasetFile = request.FILES['dataset-file']

        fs = FileSystemStorage()
        filename = fs.save(datasetFile.name, datasetFile)
        uploaded_file_url = fs.url(filename)

        try:
            result = DataWallLoader(uploaded_file_url).load(datasetDateObj)
            if result.succeeded():
                error = False
                message = "Success!"
            else:
                error = True
                message = str(len(result.failed_rows)) + " rows reported errors. Loaded " + str(result.rows_succeeded) + " successfully."

        except ValueError as e:
            error = True
            message = "This is not a valid dataset: " + str(e)

        fs.delete(datasetFile.name)

    return render(request, 'import.html', {'message': message, 'error': error, 'tab': datasetType, 'date': datasetDate})
