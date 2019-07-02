from vaga.models import VagaModel
from django.views.generic import TemplateView, ListView


# Create your views here.
class HomeListView(ListView):
    model = VagaModel
    paginate_by = 5
    template_name = 'core/index.html'


class CadastroTemplateView(TemplateView):
    template_name = 'core/cadastro.html'
