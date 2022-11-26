from rest_framework import serializers


from .models import Dado

class DadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dado
        fields = "__all__"
