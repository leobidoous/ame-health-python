from pessoa.models import User
from django.db import models


# Create your models here.
class VagaModel(models.Model):
    title = models.CharField(max_length=255)
    state = models.CharField(max_length=2)
    city = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    enterprise = models.CharField(max_length=255)
    description = models.TextField(max_length=1000)
    dt_create = models.DateTimeField(auto_now_add=True)
    dt_update = models.DateTimeField(auto_now=True)
    dt_validate = models.DateField()

    class Meta:
        verbose_name = 'Vaga'
        verbose_name_plural = 'Vagas'
        ordering = ['dt_update']

    def __str__(self):
        return self.title
