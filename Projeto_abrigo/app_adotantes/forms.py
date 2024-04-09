from django import forms
from app_adotantes.models import Form_User

class UserForm (forms.ModelForm):
    class Meta:
         model = Form_User
         fields = ["nome", "email", "telefone", "quant_animais", "info_geral"]
