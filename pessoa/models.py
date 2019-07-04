# coding=utf-8
from django.contrib.auth.models import AbstractBaseUser, UserManager, PermissionsMixin
from django.core import validators
from django.db import models
import re


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(
        'Username', max_length=30, unique=True, validators=[
            validators.RegexValidator(
                re.compile('^[\w.@+-]+$'),
                'Informe um nome de usuário válido. '
                'Este valor deve conter apenas letras, números '
                'e os caracteres: @/./+/-/_ .'
                , 'invalid'
            )
        ], help_text='Um nome curto que será usado para identificá-lo de forma única na plataforma'
    )
    name = models.CharField('Name', max_length=255, blank=False)
    email = models.EmailField('E-mail Address', unique=True)
    cpf = models.CharField('CPF', max_length=14, unique=True)
    is_staff = models.BooleanField('Team', default=False)
    is_active = models.BooleanField('Active', default=True)
    date_joined = models.DateTimeField('Date Joined', auto_now_add=True)

    types = (('Candidato', 'Candidato'),
             ('Gestor', 'Gestor'))
    type = models.CharField('Type', max_length=10, choices=types, blank=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['name', 'cpf', 'email']

    objects = UserManager()

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'

    def __str__(self):
        return self.name or self.username

    def get_full_name(self):
        return str(self)

    def get_short_name(self):
        return str(self).split(" ")[0]


class CurriculoModel(models.Model):
    sexes = (('Masculino', 'Masculino'),
             ('Feminino', 'Feminino'),
             ('Outro', 'Outro'))

    states = (('GO', 'GO'),
              ('TO', 'TO'),
              ('PA', 'PA'),
              ('DF', 'DF'),
              ('MS', 'MS'))
    name = models.CharField('Nome', max_length=255)
    cpf = models.CharField('CPF', max_length=14, unique=True)
    cel = models.CharField('Celular', max_length=14)
    birth = models.DateTimeField('Nascimento')
    genre = models.CharField('Gênero', max_length=10, choices=sexes, blank=True)
    address = models.CharField('Endereço', max_length=255)
    complement = models.CharField('Complemento', max_length=255)
    city = models.CharField('Cidade', max_length=50)
    state = models.CharField('Estado', max_length=2, choices=states)
    cep = models.CharField('Gênero', max_length=8)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    dt_create = models.DateTimeField('Criado em:', auto_now_add=True)
    dt_update = models.DateTimeField('Atualizado em:', auto_now=True)

    class Meta:
        verbose_name = 'Currículo'
        verbose_name_plural = 'Currículos'
        ordering = ['name']

    def __str__(self):
        return self.name

