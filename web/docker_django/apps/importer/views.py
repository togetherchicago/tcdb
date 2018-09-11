from django.shortcuts import render, redirect
from redis import Redis
from django.core.files.storage import FileSystemStorage
import csv
from datetime import datetime

redis = Redis(host='redis', port=6379)

def importer(request):

    error = False
    message = None
    datasetType = 'wr'

    if request.method == 'POST':
        datasetType = request.POST['dataset-type']
        datasetDate = request.POST['dataset-date']

        try:
            datasetDateObj = datetime.strptime(datasetDate, '%m/%d/%Y')
        except ValueError:
            return render(request, 'import.html', {'message': 'Please choose a date.', 'error': 'true', 'tab': datasetType})

        if 'dataset-file' not in request.FILES:
            return render(request, 'import.html', {'message': 'Please choose a file.', 'error': 'true', 'tab': datasetType})

        datasetFile = request.FILES['dataset-file']

        fs = FileSystemStorage()
        filename = fs.save(datasetFile.name, datasetFile)
        uploaded_file_url = fs.url(filename)

        with open(uploaded_file_url, mode='r') as infile:
            reader = csv.reader(infile)
            mydict = dict(row[:2] for row in reader if row)
            print(mydict)

        fs.delete(datasetFile.name)

        message = "Success!"

    return render(request, 'import.html', {'message': message, 'error': error, 'tab': datasetType})
