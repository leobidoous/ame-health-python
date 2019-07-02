from django import forms


class CandidatoForm(forms.Form):
    name = forms.CharField(label='Nome')
    cpf = forms.CharField(label='CPF')
