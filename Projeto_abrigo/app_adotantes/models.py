from django.db import models
from app_animais.models import Animal
from app_voluntarios.models import Voluntario
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Form_User(models.Model):
    nome = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    telefone =PhoneNumberField()
    quant_animais = models.CharField(max_length=500)
    info_geral = models.CharField(max_length=500)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'adotante'
        verbose_name_plural = 'adotantes'

STATUS = (
    ('p', 'Pendente'),
    ('a', 'Aprovado'),
    ('r', 'Recusado'),
)

class Adocao(models.Model):
    status = models.CharField(max_length=1, choices=STATUS, default='p')
    data = models.DateTimeField('criado em',auto_now_add=True)
    animal = models.ForeignKey(Animal, on_delete = models.CASCADE)
    voluntario = models.ForeignKey(Voluntario, on_delete = models.CASCADE)
    adotante = models.ForeignKey(Form_User, verbose_name='adotante',related_name='pedido', on_delete = models.CASCADE)
    
#ordena lista de pedidos de adoção

    class Meta:
        ordering = ('-pk',)
        verbose_name = 'Pedido de adoção'
        verbose_name_plural = 'Pedidos de adoção'

    def __str__(self):
        return f'{(self.pk)}-{self.animal}'

