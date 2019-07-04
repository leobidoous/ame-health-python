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
from django.conf.urls import url, include
from django.urls import path

from core.views import VagaListView
from vaga.models import VagaModel
from vaga.views import VagasView
from rest_framework import routers, serializers, viewsets

# Serializers define the API representation.
class VagaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = VagaModel
        fields = ('title', 'state', 'city', 'enterprise', 'description', 'dt_validate')

# ViewSets define the view behavior.
class VagaViewSet(viewsets.ModelViewSet):
    queryset = VagaModel.objects.all()
    serializer_class = VagaSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'vagas', VagaViewSet)


app_name = 'vaga'

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url('', include(router.urls)),
    url('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url('rest_vagas/', VagasView.as_view(), name='rest_vagas'),
    path('<slug:slug>/', VagaListView.as_view(), name='vaga_page'),

]

