from django.shortcuts import render
from django.http import HttpResponse 

def inicial(request):
    return render(request, 'inicial.html')

def sobre(request):
    return render(request, 'sobre.html')
