from django.forms import ModelForm
from vaga.models import VagaModel

class VagaForm(ModelForm):

    class Meta:
        model = VagaModel
        fields = ['title', 'state', 'city', 'enterprise', 'description', 'dt_validate']