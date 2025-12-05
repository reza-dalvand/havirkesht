from rest_framework import serializers
from .models import (
    PurityPrice, ProductPrice, FarmersPayment, FarmersInvoicePayed,
    FarmersGuarantee, FactoryPayment
)

class PurityPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurityPrice
        fields = "__all__"

class ProductPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductPrice
        fields = "__all__"

class FarmersPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = FarmersPayment
        fields = "__all__"

class FarmersInvoicePayedSerializer(serializers.ModelSerializer):
    class Meta:
        model = FarmersInvoicePayed
        fields = "__all__"

class FarmersGuaranteeSerializer(serializers.ModelSerializer):
    class Meta:
        model = FarmersGuarantee
        fields = "__all__"

class FactoryPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = FactoryPayment
        fields = "__all__"