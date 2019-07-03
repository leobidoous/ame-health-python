from django.contrib.auth.forms import PasswordChangeForm
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from pessoa.forms import UserAdminCreationForm
from django.urls import reverse_lazy
from vaga.models import VagaModel
from pessoa.models import User


# Create your views here.
class HomeListView(ListView):
    model = VagaModel
    paginate_by = 5
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
    fields = ['name', 'email']
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


# GESTOR VIEW ###################################################################
class CadastroGestorCreateView(LoginRequiredMixin, CreateView):
    form_class = UserAdminCreationForm
    template_name = 'core/cadastro_gestor.html'

    def get_object(self):
        return self.request.user


class UpdateGestorUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    template_name = 'core/update_gestor.html'
    fields = ['name', 'email', 'type']
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


# GERAL ###################################################################
class PerfilTemplateView(LoginRequiredMixin, TemplateView):
    template_name = 'core/perfil.html'


