from django.shortcuts import render
from .models import Cards

def cards(request):
    selected_category = request.GET.get('category')
    if selected_category:
        cards = Cards.objects.filter(category=selected_category)
    else:
        cards = Cards.objects.all()
    categories = set(card.category for card in Cards.objects.all())
    context = {
        'cards': cards,
        'categories': categories,
        'selected_category': selected_category,
    }
    return render(request, 'cards/cards.html', context)