from django.shortcuts import render
from .models import History

# def my_history(request):
#     history_events = History.objects.all()
#     return render(request, 'history.html', {'history_events': history_events})

def history(request):
    return render(request, 'history/history.html')
