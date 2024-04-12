from django.shortcuts import render, get_object_or_404
from app_animais.models import Animal

def animal_list(request):
    animais_disponiveis = Animal.objects.filter(disponivel=True)
    return render(request, 'animais.html', {'animais': animais_disponiveis})

def animal_detail(request, pk):
    animal = get_object_or_404(Animal, pk=pk)
    return render(request, 'animal_detail.html', {'animal': animal})

def animal_filter(request):
    if 'especie' in request.GET:
        especie = request.GET('especie', '')
        animais = Animal.objects.filter(especie_contains=especie)
    else:
        animais = Animal.objects.all()
    contexto = {'animais': animais}
    
    return render(request, 'animais.html', contexto)