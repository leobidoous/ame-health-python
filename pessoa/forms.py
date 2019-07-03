# coding=utf-8
from django.contrib.auth.forms import UserCreationForm
from pessoa.models import User
from django import forms


class UserAdminCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['name', 'cpf', 'username', 'email', 'type']


class UserAdminForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username', 'email', 'name', 'is_active', 'is_staff', 'type']
