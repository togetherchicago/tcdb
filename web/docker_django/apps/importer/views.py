from django.shortcuts import render
from redis import Redis
from django.core.files.storage import FileSystemStorage
import csv
from datetime import datetime

from library.DataWallLoader import DataWallLoader

redis = Redis(host='redis', port=6379)

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

        csv_data = csv.DictReader(open(uploaded_file_url))

        # with open(uploaded_file_url, mode='r') as infile:
        #     reader = csv.reader(infile)
        #     mydict = dict(row for row in reader if row)

        DataWallLoader().load(csv_data, datasetDateObj)
        fs.delete(datasetFile.name)

        message = "Success!"

    return render(request, 'import.html', {'message': message, 'error': error, 'tab': datasetType, 'date': datasetDate})
