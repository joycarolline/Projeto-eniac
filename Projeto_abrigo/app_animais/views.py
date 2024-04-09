from django.shortcuts import render , get_object_or_404
from app_animais.models import Animal

def animais(request):
    animais = Animal.objects.all()
    return render(request, 'animais.html', {'animais': animais})
def animal_detail(request, pk):
    animal = get_object_or_404(Animal, pk=pk)
    return render(request, 'animais_detalhes.html', {'animal': animal})