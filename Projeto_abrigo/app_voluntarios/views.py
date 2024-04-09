from django.shortcuts import render

# Create your views here.
def voluntarios(request):
    return render(request, 'voluntarios.html')