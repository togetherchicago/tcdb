from django.shortcuts import render, redirect
from redis import Redis


redis = Redis(host='redis', port=6379)


def home(request):
    return render(request, 'import.html')
