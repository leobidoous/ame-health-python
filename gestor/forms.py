from django import forms


class GestorForm(forms.Form):
    name = forms.CharField(name='Nome')
    cpf = forms.CharField(name='CPF')