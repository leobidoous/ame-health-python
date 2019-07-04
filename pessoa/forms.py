# coding=utf-8
from django.contrib.auth.forms import UserCreationForm
from pessoa.models import User, CurriculoModel
from django import forms

class UserAdminCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['name', 'cpf', 'username', 'email', 'type']


class UserAdminForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username', 'email', 'name', 'is_active', 'is_staff', 'type']



class CurriculoForm(forms.ModelForm):

    class Meta:
        model = CurriculoModel
        fields = ['name', 'cpf', 'birth', 'genre', 'cel']