from django.shortcuts import render
from django.http import HttpResponse 
from app_adotantes.forms import UserForm, AdocaoForm
from app_adotantes.models import Form_User, Adocao

def listar_user(request):
    users = Form_User.objects.all()
    return render(request, 'user.html', {'users': users})


def cadastrar_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = UserForm()
    
    return render(request, 'form_user.html', {'form': form})


def editar_user(request, user_id):
    user = Form_User.objects.get(pk=user_id)
    
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
    else:
        form = UserForm(instance=user)
    
    return render(request, 'form_user.html', {'form': form})


def excluir_user(request, user_id):
    user = Form_User.objects.get(pk=user_id)
    user.delete()
    return render(request, 'user.html')


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
