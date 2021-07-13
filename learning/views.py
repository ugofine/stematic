from events.models import Event
from stematic.models import Stem
from django.shortcuts import render
from blog.models import Blog
from django.contrib.auth.models import User



# Create your views here.

def home(request):
    stematic = Stem.objects.all()
    events = Event.objects.all()
    blogs = Blog.objects.all()
    return render(request, 'pages/index.html', {'stematic': stematic, 'events': events, 'blogs': blogs})
    

def about(request):
    return render(request, 'pages/about.html')

def courses(request):
    stematic = Stem.objects.all()
    return render(request, 'pages/courses.html', {'stematic': stematic})

def events(request):
    return render(request, 'pages/events.html')
   

def contact(request):
    return render(request, 'pages/contact.html')

def blog(request):
    return render(request, '/blog.html')   

