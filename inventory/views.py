from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import (
    Seed, Pesticide, FactorySeed, FactoryPesticide, 
    FarmersSeed, FarmersPesticide, FactorySugar, FactoryWaste, 
    FarmersSugarDelivery, FarmersWasteDelivery
)
from .serializers import *
from common.pagination import CustomPagination 

class SeedViewSet(viewsets.ModelViewSet):
    queryset = Seed.objects.all()
    serializer_class = SeedSerializer
    lookup_field = 'id'
    pagination_class = CustomPagination
    permission_classes = [IsAuthenticated]


class PesticideViewSet(viewsets.ModelViewSet):
    queryset = Pesticide.objects.all()
    serializer_class = PesticideSerializer
    lookup_field = 'id'
    pagination_class = CustomPagination
    permission_classes = [IsAuthenticated]

class FactorySeedViewSet(viewsets.ModelViewSet):
    queryset = FactorySeed.objects.all()
    serializer_class = FactorySeedSerializer
    lookup_field = 'id'
    pagination_class = CustomPagination
    permission_classes = [IsAuthenticated]
    filterset_fields = ['factory', 'crop_year', 'seed']


class FactoryPesticideViewSet(viewsets.ModelViewSet):
    queryset = FactoryPesticide.objects.all()
    serializer_class = FactoryPesticideSerializer
    lookup_field = 'id'
    pagination_class = CustomPagination
    permission_classes = [IsAuthenticated]
    filterset_fields = ['factory', 'crop_year', 'pesticide']

class FarmersSeedViewSet(viewsets.ModelViewSet):
    queryset = FarmersSeed.objects.all()
    serializer_class = FarmersSeedSerializer
    lookup_field = 'id'
    pagination_class = CustomPagination
    permission_classes = [IsAuthenticated]
    filterset_fields = ['commitment__farmer', 'crop_year', 'factory']


class FarmersPesticideViewSet(viewsets.ModelViewSet):
    queryset = FarmersPesticide.objects.all()
    serializer_class = FarmersPesticideSerializer
    lookup_field = 'id'
    pagination_class = CustomPagination
    permission_classes = [IsAuthenticated]
    filterset_fields = ['commitment__farmer', 'crop_year', 'factory']



class FactorySugarViewSet(viewsets.ModelViewSet):
    queryset = FactorySugar.objects.all()
    serializer_class = FactorySugarSerializer
    lookup_field = 'id'
    pagination_class = CustomPagination
    permission_classes = [IsAuthenticated]
    filterset_fields = ['factory', 'crop_year']


class FactoryWasteViewSet(viewsets.ModelViewSet):
    queryset = FactoryWaste.objects.all()
    serializer_class = FactoryWasteSerializer
    lookup_field = 'id'
    pagination_class = CustomPagination
    permission_classes = [IsAuthenticated]
    filterset_fields = ['factory', 'crop_year']


class FarmersSugarDeliveryViewSet(viewsets.ModelViewSet):
    queryset = FarmersSugarDelivery.objects.all()
    serializer_class = FarmersSugarDeliverySerializer
    lookup_field = 'id'
    pagination_class = CustomPagination
    permission_classes = [IsAuthenticated]
    filterset_fields = ['farmer', 'crop_year']


class FarmersWasteDeliveryViewSet(viewsets.ModelViewSet):
    queryset = FarmersWasteDelivery.objects.all()
    serializer_class = FarmersWasteDeliverySerializer
    lookup_field = 'id'
    pagination_class = CustomPagination
    permission_classes = [IsAuthenticated]
    filterset_fields = ['farmer', 'crop_year']