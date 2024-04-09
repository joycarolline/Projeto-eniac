from django.contrib import admin
from .models import Voluntario,PedidoInscricao
from phonenumber_field.widgets import PhoneNumberPrefixWidget
from django import forms

# Register your models here.

class ContactForm(forms.ModelForm):
    class Meta:
        widgets = {
            'telefone': PhoneNumberPrefixWidget(initial='BR'),
        }

@admin.register(Voluntario)
class AdocaoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'telefone')
    form = ContactForm

@admin.register(PedidoInscricao)
class PedidoAdmin(admin.ModelAdmin):
    search_fields = ['status']
