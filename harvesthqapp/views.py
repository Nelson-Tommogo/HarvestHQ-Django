from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse('<h1>HarvestHQ Home</h>')


def about(request):
    return HttpResponse('<h1>HarvestHQ Activies</h1>')