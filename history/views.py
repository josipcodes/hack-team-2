from django.shortcuts import render
from .models import History

def history(request):
    history_events = History.objects.all()
    return render(request, 'history/history.html', {'history_events': history_events})