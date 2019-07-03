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
from django.urls import path
from core.views import *
app_name = 'core'


urlpatterns = [
    path('', HomeListView.as_view(), name='home'),
    path('login/', LoginView.as_view(template_name='core/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='core:home'), name='logout'),
    path('perfil/', PerfilTemplateView.as_view(), name='perfil'),
    path('cadastro_gestor/', CadastroGestorFormView.as_view(), name='cadastro_gestor'),
    path('cadastro_candidato/', CadastroCandidatoFormView.as_view(), name='cadastro_candidato'),

]

