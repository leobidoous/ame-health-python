from rest_framework import serializers
from pessoa.models import User

class PessoaModelSerializer(serializers.ModelSerializer):

    class Meta:

        model = User
        fields = '__all__'