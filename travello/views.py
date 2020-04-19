from django.shortcuts import render
from .models import Destinations

# Create your views here.

def index(request):
    dest1 = Destinations()
    dest1.name = 'Mumbai'
    dest1.desc = "The city which never sleeps."
    
    return render(request, "index.html", {'dest1': dest1})
