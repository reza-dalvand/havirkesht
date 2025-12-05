from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import (
    PurityPrice, ProductPrice, FarmersPayment, FarmersInvoicePayed, 
    FarmersGuarantee, FactoryPayment
)
from .serializers import (
    PurityPriceSerializer, ProductPriceSerializer, FarmersPaymentSerializer, 
    FarmersInvoicePayedSerializer, FarmersGuaranteeSerializer, FactoryPaymentSerializer
)
from common.pagination import CustomPagination 


class PurityPriceViewSet(viewsets.ModelViewSet):
    queryset = PurityPrice.objects.all()
    serializer_class = PurityPriceSerializer
    lookup_field = 'id'
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPagination

class ProductPriceViewSet(viewsets.ModelViewSet):
    queryset = ProductPrice.objects.all()
    serializer_class = ProductPriceSerializer
    lookup_field = 'id'
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPagination

class FarmersPaymentViewSet(viewsets.ModelViewSet):
    queryset = FarmersPayment.objects.all()
    serializer_class = FarmersPaymentSerializer
    lookup_field = 'id'
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPagination

class FarmersInvoicePayedViewSet(viewsets.ModelViewSet):
    queryset = FarmersInvoicePayed.objects.all()
    serializer_class = FarmersInvoicePayedSerializer
    lookup_field = 'id'
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPagination

class FarmersGuaranteeViewSet(viewsets.ModelViewSet):
    queryset = FarmersGuarantee.objects.all()
    serializer_class = FarmersGuaranteeSerializer
    lookup_field = 'id'
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPagination

class FactoryPaymentViewSet(viewsets.ModelViewSet):
    queryset = FactoryPayment.objects.all()
    serializer_class = FactoryPaymentSerializer
    lookup_field = 'id'
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPagination