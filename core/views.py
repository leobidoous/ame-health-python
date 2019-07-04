from django.contrib.auth.forms import PasswordChangeForm
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from pessoa.forms import UserAdminCreationForm
from django.urls import reverse_lazy
from vaga.models import VagaModel
from vaga.forms import VagaForm
from pessoa.forms import CurriculoForm
from pessoa.models import User, CurriculoModel


# Create your views here.
class HomeListView(ListView):
    model = VagaModel
    # paginate_by = 5
    template_name = 'core/index.html'

# CANDIDATO VIEW ###################################################################
class CadastroCandidatoCreateView(CreateView):
    model = User
    template_name = 'core/cadastro_candidato.html'
    form_class = UserAdminCreationForm
    success_url = reverse_lazy('core:perfil')


class UpdateCandidatoUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    template_name = 'core/update_candidato.html'
    fields = ['name', 'email', 'cpf']
    success_url = reverse_lazy('core:perfil')

    def get_object(self):
        return self.request.user


class UpdatePasswordCandidatoFormVieW(LoginRequiredMixin, FormView):
    template_name = 'core/update_password_candidato.html'
    success_url = reverse_lazy('core:perfil')
    form_class = PasswordChangeForm

    def get_form_kwargs(self):
        kwargs = super(UpdatePasswordCandidatoFormVieW, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class VagaCandidatoListView(ListView):
    model = VagaModel
    paginate_by = 5
    template_name = 'core/gerenciar_vagas_candidato.html'


class CurriculoCandidatoListView(ListView):
    model = CurriculoModel
    template_name = 'core/curriculo_candidato.html'


class NovoCurriculoCreateView(LoginRequiredMixin, FormView):
    form_class = CurriculoForm
    template_name = 'core/novo_curriculo.html'
    success_url = reverse_lazy('core:perfil')

    def form_valid(self, form):
        print(self.request.user)
        curriculo = form.save(commit=False)
        curriculo.author = self.request.user
        form.save()
        return super(NovoCurriculoCreateView, self).form_valid(form)


# GESTOR VIEW ###################################################################
class CadastroGestorCreateView(LoginRequiredMixin, CreateView):
    form_class = UserAdminCreationForm
    template_name = 'core/cadastro_gestor.html'

    def get_object(self):
        return self.request.user


class UpdateGestorUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    template_name = 'core/update_gestor.html'
    fields = ['name', 'email', 'cpf', 'type']
    success_url = reverse_lazy('core:perfil')

    def get_object(self):
        return self.request.user


class UpdatePasswordGestorFormVieW(LoginRequiredMixin, FormView):
    template_name = 'core/update_password_gestor.html'
    success_url = reverse_lazy('core:perfil')
    form_class = PasswordChangeForm

    def get_form_kwargs(self):
        kwargs = super(UpdatePasswordGestorFormVieW, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class VagasGestorCreateView(LoginRequiredMixin, FormView):
    form_class = VagaForm
    template_name = 'core/gerenciar_vagas_gestor.html'
    success_url = reverse_lazy('core:perfil')

    def form_valid(self, form):
        vaga = form.save(commit=False)
        vaga.author = self.request.user
        form.save()
        return super(VagasGestorCreateView, self).form_valid(form)


class VagaListView(ListView):
    model = VagaModel
    template_name = 'core/vaga_page.html'


# GERAL ###################################################################
class PerfilTemplateView(LoginRequiredMixin, TemplateView):
    template_name = 'core/perfil.html'
