from django.shortcuts import render, get_object_or_404
from app_animais.models import Animal

def animal_list(request):
    animais = Animal.objects.all()
    return render(request, 'animais.html', {'animais': animais})

def animal_detail(request, pk):
    animal = get_object_or_404(Animal, pk=pk)
    return render(request, 'animais_detail.html', {'animal': animal})