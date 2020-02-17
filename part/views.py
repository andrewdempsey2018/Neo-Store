from django.shortcuts import render
from django.http import HttpResponse

# Import the Part model for use
from .models import Part

def index(request):
    # Query the database and pull a set of all the objects contained
    parts = Part.objects.all()
    # Pass the 'parts' set to the 'allparts' template for display
    return render(request, 'allparts.html', {'parts': parts})
