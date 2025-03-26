from django.shortcuts import render
from .models import Destination  # Ensure the correct import

def index(request): 
    # Fetch data from the database instead of creating instances manually
    dests = Destination.objects.all()  # Fetch all destinations from the database
    return render(request, 'index.html', {'dests': dests})  # Pass list of destinations