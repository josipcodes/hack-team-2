from django.shortcuts import render
from .models import Cards
import random

def cards(request):
    selected_category = request.GET.get('category')
    if selected_category:
        cards = list(Cards.objects.filter(category=selected_category))
    else:
        cards = list(Cards.objects.all())
    
    random.shuffle(cards) 

    categories = set(card.category for card in Cards.objects.all())
    context = {
        'cards': cards,
        'categories': categories,
        'selected_category': selected_category,
    }
    return render(request, 'cards/cards.html', context)