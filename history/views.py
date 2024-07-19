from django.shortcuts import render
from django.http import HttpResponse

def my_history(request):
    return HttpResponse("Hello, History Timeline!")
