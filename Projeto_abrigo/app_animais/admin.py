from django.contrib import admin
from .models import Animal, Historico_medico,Raca,Porte,Especie,Sexo

# Register your models here.
@admin.register(Raca)
class AnimalAdmin(admin.ModelAdmin):
    list_display = ['raca']
    search_fields = ['raca']

@admin.register(Porte)
class AnimalAdmin(admin.ModelAdmin):
    list_display = ['porte']
    search_fields = ['porte']

@admin.register(Especie)
class EspecieAdmin(admin.ModelAdmin):
    list_display = ['especie']
    search_fields = ['especie']

@admin.register(Sexo)
class SexoAdmin(admin.ModelAdmin):
    list_display = ['sexo']
    search_fields = ['sexo']

@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    list_display = ('nome', 'especie', 'raca')
    search_fields = ['nome', 'especie', 'raca', 'porte', 'sexo' ]

@admin.register(Historico_medico)
class HistoricoAdmin(admin.ModelAdmin):
    list_display = ('animal', 'data')
    search_fields = ['nome', 'especie', 'raca', 'porte', 'sexo', 'data' ]