from django.shortcuts import render
from django.http import HttpResponse

def history(request):
    return HttpResponse("Hello, History Timeline!")
