from django.shortcuts import render
from django.http import HttpResponse 

# Create your views here.
def adotantes(request):
    return render(request, 'adotantes.html')