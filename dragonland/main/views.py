from django.shortcuts import render
# Create your views here.

def index(request):
    return render(request, 'main/index.html')

def reserve(request):
    return render(request, 'main/reserve.html')

def to_do(request):
    return render(request, 'main/to-do.html')

def map(request):
    return render(request, 'main/map.html')