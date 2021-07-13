from django.shortcuts import render
from .models import Event

# Create your views here.

def event(request):
    events = Event.objects.all()
    return render(request, 'pages/events.html', {'events': events})

