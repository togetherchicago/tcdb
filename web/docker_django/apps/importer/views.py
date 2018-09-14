from datetime import datetime

from django.core.files.storage import FileSystemStorage
from django.shortcuts import render

from library.DataWallLoader import DataWallLoader
from library.RosterLoader import RosterLoader


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
            if datasetType == 'wr':
                result = RosterLoader(uploaded_file_url).load(datasetDateObj)
            elif datasetType == 'dw':
                result = DataWallLoader(uploaded_file_url).load(datasetDateObj)

            if result.succeeded():
                error = False
                message = str(len(result.failed_rows)) + " records loaded successfully."
            else:
                error = True
                message = str(len(result.failed_rows)) + " records failed. Loaded " + str(result.rows_succeeded) + " records successfully."

        except ValueError as e:
            error = True
            message = "This is not a valid dataset: " + str(e) + " No data was loaded in the database."

        fs.delete(datasetFile.name)

    return render(request, 'import.html', {'message': message, 'error': error, 'tab': datasetType, 'date': datasetDate})
