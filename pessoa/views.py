from rest_framework import generics
from pessoa.models import User
from pessoa.serializers import PessoaModelSerializer


# Create your views here.
class PessoaView(generics.ListCreateAPIView):

    queryset = User.objects.all()
    serializer_class = PessoaModelSerializer