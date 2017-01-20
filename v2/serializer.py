from rest_framework import serializers

from generator.models import Esc


class EscenarioSerializer(serializers.Serializer):
    created_at = serializers.DateTimeField(source='criado_em')
    title = serializers.CharField(max_length=30, source='esc.titulo')
    image_url = serializers.URLField(source='img_id')
    votes = serializers.IntegerField(source='votos')


class CreateEscenarioSerializer(serializers.ModelSerializer):
    autonumber = serializers.BooleanField(read_only=True)

    class Meta:
        model = Esc
        fields = ('titulo', 'faltam', 'descricao', 'autonumber')
