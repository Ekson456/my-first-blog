from django.shortcuts import render
from django.http import HttpResponse

def hello(request):
    return HttpResponse("hello again")

# Create your views here.
