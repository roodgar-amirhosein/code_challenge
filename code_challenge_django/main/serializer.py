from rest_framework import serializers
from .models import Orders


class BuyStockSerializer(serializers.Serializer):
    user = serializers.CharField()
    stockname = serializers.CharField()
    quantity = serializers.IntegerField()


class OrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = '__all__'
