from django.db import models


# Create your models here.
class GestorModel(models.Model):
    name = models.CharField('Nome', max_length=255)
    cpf = models.CharField('CPF', max_length=14, unique=True)
    dt_create = models.DateTimeField('Criado em:', auto_now_add=True)
    dt_update = models.DateTimeField('Atualizado em:', auto_now=True)

    class Meta:
        verbose_name = 'Gestor'
        verbose_name_plural = 'Gestores'
        ordering = ['name']

    def __str__(self):
        return self.name
