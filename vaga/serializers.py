from rest_framework import serializers
from vaga.models import VagaModel

class VagaModelSerializer(serializers.ModelSerializer):

    class Meta:

        model = VagaModel
        fields = '__all__'