# coding=utf-8

from django.db import models
from django.core import validators
from django.contrib.auth.models import AbstractBaseUser, UserManager, PermissionsMixin
import re


class User(AbstractBaseUser, PermissionsMixin):

    username = models.CharField(
        'Apelido / Usuário', max_length=30, unique=True, validators=[
            validators.RegexValidator(
                re.compile('^[\w.@+-]+$'),
                'Informe um nome de usuário válido. '
                'Este valor deve conter apenas letras, números '
                'e os caracteres: @/./+/-/_ .'
                , 'invalid'
            )
        ], help_text='Um nome curto que será usado para identificá-lo de forma única na plataforma'
    )
    name = models.CharField('Nome', max_length=255, blank=True)
    email = models.EmailField('E-mail', unique=True)
    is_staff = models.BooleanField('Equipe', default=False)
    is_active = models.BooleanField('Ativo', default=True)
    date_joined = models.DateTimeField('Data de Entrada', auto_now_add=True)

    password = models.CharField('Senha', max_length=255)
    cpf = models.CharField('CPF', max_length=14, unique=True)

    types = (('1', 'CANDIDATO'),
             ('2', 'GESTOR'))
    type = models.CharField('Tipo', max_length=10, choices=types, default='1')

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['cpf', 'email']

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
    name = models.CharField('Nome', max_length=255)
    cpf = models.CharField('CPF', max_length=14, unique=True)
    dt_create = models.DateTimeField('Criado em:', auto_now_add=True)
    dt_update = models.DateTimeField('Atualizado em:', auto_now=True)

    class Meta:
        verbose_name = 'Currículo'
        verbose_name_plural = 'Currículos'
        ordering = ['name']

    def __str__(self):
        return self.name