from django.contrib import admin
from .models import Form_User
from phonenumber_field.widgets import PhoneNumberPrefixWidget
from django import forms

# Register your models here.
class ContactForm(forms.ModelForm):
    class Meta:
        widgets = {
            'telefone': PhoneNumberPrefixWidget(initial='BR'),
        }


@admin.register(Form_User)
class AdotanteAdmin(admin.ModelAdmin):
    list_display = ('animal', 'nome_adotante', 'telefone_adotante', 'status', 'data')
    search_fields = ['animal','nome_adotante', 'telefone_adotante','email_adotante']
    form = ContactForm
    list_filter = ('status',)
    date_hierarchy = 'data'


    