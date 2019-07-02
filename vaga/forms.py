from django import forms


class VagaForm(forms.Form):
    title = forms.CharField(name='Título')
    describle = forms.CharField(name='Descrição', widget=forms.Textarea)
    dt_validate = forms.DateField(name='Data de Validade')