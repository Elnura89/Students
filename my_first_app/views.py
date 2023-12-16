from django.shortcuts import render
# from django.http import HttpResponse
from .models import *
# Create your views here.



def index(request):
    
    rows = Students.objects.all()
    context = {
        'rows':rows
    }
    return render(request, 'index.html', context)


def contact(request):
    if request. method == 'POST':
        name = request.POST.get('name')
        nomer=request.POST.get('nomer')
        Students.objects.create(name=name, nomer=nomer)
        return index(request)
    return render(request, 'contact.html')


