from django import forms


class VagaForm(forms.Form):

    title = forms.CharField(label='Title', max_length=255)
    state = forms.CharField(label='State', max_length=2)
    city = forms.CharField(label='City', max_length=100)
    enterprise = forms.CharField(label='Enterprise', max_length=255)
    descrition = forms.ChoiceField(label='Descrition', max_length=1000, widget=forms.Textarea)
    dt_validate = forms.DateTimeField(label='Validate')