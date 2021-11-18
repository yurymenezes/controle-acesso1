from django.db import models
from django.db.models.fields.related import OneToOneField

# Create your models here.

class Porteiro(models.Model):

    usuario = OneToOneField(

        "usuarios.Usuario",
        verbose_name='Usuário',
        on_delete=models.PROTECT

    )

    nome_completo = models.CharField(

        verbose_name='Nome Completo',
        max_length=194,
    )

    cpf = models.CharField(

        verbose_name='CPF',
        max_length=11,

    )

    telefone = models.CharField(

        verbose_name='Telefone de Contato',
        max_length=11,
        
    )

    data_nascimento = models.DateField(

        verbose_name='Data de Nascimento',
        auto_now=False,
        auto_now_add=False,

    )

    class Meta:

        verbose_name = 'Porteiro'
        verbose_name_plural = 'Porteiros'
        db_table = 'porteiro'

    def __str__(self):
        return self.nome_completo    