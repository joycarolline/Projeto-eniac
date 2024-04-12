from django.db import models
from app_animais.models import Animal
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

STATUS = (
    ('p', 'Pendente'),
    ('a', 'Aprovado'),
    ('r', 'Recusado'),
)

class Form_User(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.SET_NULL, null=True, blank=True)
    nome_adotante = models.CharField(max_length=50)
    email_adotante = models.EmailField(max_length=50)
    telefone_adotante =PhoneNumberField()
    quant_animais = models.CharField(max_length=500)
    info_geral_adotante = models.CharField(max_length=500)
    status = models.CharField(max_length=1, choices=STATUS, default='p')
    data = models.DateTimeField('criado em', auto_now_add=True)

    

    class Meta:
        verbose_name = 'Pedido de adoção'
        verbose_name_plural = 'Pedidos de adoção'

    def __str__(self):
        if self.animal:
            return f'{str(self.pk).zfill(3)}-{self.animal}'

        return f'{str(self.pk).zfill(3)}'




   

