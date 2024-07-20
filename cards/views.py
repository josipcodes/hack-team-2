from django.shortcuts import render
from django.http import HttpResponse

# def cards(request):
#     return HttpResponse("Hello, Ace of Spades!")

def cards(request):
    return render(request, 'cards/cards.html')
