from rest_framework import serializers


from .models import Dado

class DadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dado
        fields = "__all__"

class ListDadoSerializer(serializers.ModelSerializer):
    sale = serializers.SerializerMethodField(method_name="get_saldo_method", read_only=True)
    class Meta:
        model = Dado
        fields = ["id",
            "sale",
            "date",
            "value",
            "cpf",
            "card",
            "hour",
            'typeOp',
            "store_owner",
            "store_name",]
    def get_saldo_method(self,obj:Dado):
        return obj.get_saldo()
   
