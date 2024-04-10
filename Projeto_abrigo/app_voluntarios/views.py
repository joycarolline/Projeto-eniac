from django.shortcuts import render, redirect
from app_voluntarios.forms import VoluntariosForms

# Create your views here.
def voluntarios(request):
    if request.method == 'POST':
        form = VoluntariosForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sucesso')  # Redireciona para a página de sucesso após salvar o formulário
    else:
        form = VoluntariosForms()
    return render(request, 'voluntarios.html', {'form': form}) 


def sucesso(request):
    return render(request, 'sucesso.html') 
    