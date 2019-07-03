from vaga.models import VagaModel
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import FormView
from pessoa.forms import PessoaForm


# Create your views here.
class HomeListView(ListView):
    model = VagaModel
    paginate_by = 5
    template_name = 'core/index.html'


class CadastroCandidatoFormView(FormView):
    template_name = 'core/cadastro_candidato.html'
    form_class = PessoaForm
    success_url = '/thanks/'


class CadastroGestorFormView(FormView):
    form_class = PessoaForm
    template_name = 'core/cadastro_gestor.html'


class PerfilTemplateView(TemplateView):
    template_name = 'core/perfil.html'
