from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse 
from app_animais.models import Animal
from app_adotantes.forms import PedidoAdocaoForm
from app_adotantes.forms import AdocaoForm
from app_adotantes.models import Adocao

def formulario_animal(request, pk):
    animal = get_object_or_404(Animal, pk=pk)
    if request.method == 'POST':
        form = PedidoAdocaoForm (request.POST)
        if form.is_valid():
            form.instance.animal = animal
            form.save()
            # Redirecionar para onde quiser após salvar o formulário
            return render(request, 'adotantes.html', {'form': form, 'sucesso': True})
    else:
        form = PedidoAdocaoForm()
        form.fields['animal'].initial = animal
    return render(request, 'adotantes.html', {'form': form})

def listar_adocao(request):
    adocoes = Adocao.objects.all()
    return render(request, 'adocao.html', {'adocoes': adocoes})

def cadastrar_adocao(request):
    if request.method == 'POST':
        form = AdocaoForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = AdocaoForm()
    
    return render(request, 'form_adocao.html', {'form': form})

def editar_adocao(request, adocao_id):
    adocao = Adocao.objects.get(pk=adocao_id)
    
    if request.method == 'POST':
        form = AdocaoForm(request.POST, instance=adocao)
        if form.is_valid():
            form.save()
    else:
        form = AdocaoForm(instance=adocao)
    
    return render(request, 'form_adocao.html', {'form': form})
