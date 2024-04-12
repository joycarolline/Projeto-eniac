from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse 
from app_animais.models import Animal
from app_adotantes.forms import PedidoAdocaoForm

# Create your views here.

def formulario_animal(request, pk):
    animal = get_object_or_404(Animal, pk=pk)
    if request.method == 'POST':
        form = PedidoAdocaoForm (request.POST)
        if form.is_valid():
            form.instance.animal = animal
            form.save()
            # Redirecionar para onde quiser após salvar o formulário
            return redirect('sucesso')
    else:
        form = PedidoAdocaoForm()
        form.fields['animal'].initial = animal
    return render(request, 'adotantes.html', {'form': form})

def sucesso(request):
    return render(request, 'sucesso.html') 