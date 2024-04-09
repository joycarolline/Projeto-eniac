from django.contrib import admin
from .models import Form_User, Adocao
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
    list_display = ('nome', 'email', 'telefone')
    search_fields = ['nome', 'telefone','email' ]
    form = ContactForm


@admin.register(Adocao)
class AdocaoAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'adotante', 'status')
    search_fields = ['nome', 'telefone', ]
    list_filter = ('status',)
    date_hierarchy = 'data'