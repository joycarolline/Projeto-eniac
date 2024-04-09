from django.shortcuts import render

def animais(request):
    return render(request, 'animais.html')