# coding=utf-8

from django.contrib.auth.forms import UserCreationForm
from django import forms

from pessoa.models import User


class UserAdminCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'email', 'type']


class UserAdminForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username', 'email', 'name', 'is_active', 'is_staff', 'type']


from django import forms


class PessoaForm(forms.Form):
    types = ((1, 'CANDIDATO'),
             (2, 'GESTOR'))

    name = forms.CharField(label='Name', max_length=255)
    email = forms.EmailField(label='E-mail Address', max_length=255)
    username = forms.CharField(label='Username', max_length=30)
    password1 = forms.CharField(label='Password', max_length=255)
    password2 = forms.CharField(label='Confirm Password', max_length=255)
    cpf = forms.CharField(label='CPF', max_length=14)
    type = forms.ChoiceField(label='Type', choices=types, initial=1)