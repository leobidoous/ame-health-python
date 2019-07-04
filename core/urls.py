"""master URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include
from core.views import *
app_name = 'core'


urlpatterns = [
    path('', HomeListView.as_view(), name='home'),

    path('perfil/', PerfilTemplateView.as_view(), name='perfil'),
    path('logout/', LogoutView.as_view(next_page='core:home'), name='logout'),
    path('login/', LoginView.as_view(template_name='core/login.html'), name='login'),

    path('cadastro_gestor/', CadastroGestorCreateView.as_view(), name='cadastro_gestor'),
    path('update_gestor/', UpdateGestorUpdateView.as_view(), name='update_gestor'),
    path('update_password_gestor/', UpdatePasswordGestorFormVieW.as_view(), name='update_password_gestor'),
    path('vagas_candidato/', VagaCandidatoListView.as_view(), name='vagas_candidato'),
    path('curriculo_candidato/', CurriculoCandidatoListView.as_view(), name='curriculo_candidato'),
    path('new_curriculo/', NovoCurriculoCreateView.as_view(), name='new_curriculo'),
    # path('update_curriculo/', VagaCandidatoListView.as_view(), name='update_curriculo'),

    path('cadastro_candidato/', CadastroCandidatoCreateView.as_view(), name='cadastro_candidato'),
    path('update_candidato/', UpdateCandidatoUpdateView.as_view(), name='update_candidato'),
    path('update_password_candidato/', UpdatePasswordCandidatoFormVieW.as_view(), name='update_password_candidato'),
    path('vagas_gestor/', VagasGestorCreateView.as_view(), name='vagas_gestor'),


]

