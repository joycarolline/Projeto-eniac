from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class Voluntario(models.Model):
    nome = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    telefone = PhoneNumberField()
    profissão = models.CharField(max_length=500)
    info_geral = models.CharField('Informação', max_length=500)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome
    
STATUS = (
    ('p', 'Pendente'),
    ('a', 'Aprovado'),
    ('r', 'Recusado'),
)
    
class PedidoInscricao(models.Model):
    voluntario = models.ForeignKey(Voluntario, on_delete=models.CASCADE)
    status = models.CharField(max_length=1,choices=STATUS, default="p")

    def __str__(self):
        return f"{self.voluntario}"
    
    class Meta:
        verbose_name = 'pedido de inscrição'
        verbose_name_plural = 'pedidos de inscrição'