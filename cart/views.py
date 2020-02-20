from django.shortcuts import render
from django.http import HttpResponse

# Import the Part model for use
from part.models import Part

def cart(request):
    #part = Part.objects.get(id=request.GET.get('id'))
    #return render(request, 'cart.html', {'part': part})
    return render(request, 'cart.html')