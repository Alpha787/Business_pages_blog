from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, World! There will be post's page.")
