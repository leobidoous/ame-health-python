from django.db import models

# Create your models here.
class VagaModel(models.Model):
    titulo = models.CharField(max_length=255)
    descricao = models.TextField(max_length=1000)
    dt_criacao = models.DateTimeField(auto_now_add=True)
    dt_modificacao = models.DateTimeField(auto_now=True)
    dt_validade = models.DateField()

    class Meta:
        verbose_name = 'Vaga'
        verbose_name_plural = 'Vagas'
        ordering = ['dt_modificacao']