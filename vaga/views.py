from rest_framework import generics
from vaga.models import VagaModel
from vaga.serializers import VagaModelSerializer

# Create your views here.

# Create your views here.
class VagasView(generics.ListCreateAPIView):

    queryset = VagaModel.objects.all()
    serializer_class = VagaModelSerializer