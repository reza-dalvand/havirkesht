from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import (
    Car, Driver, Carriage, CarriageStatus, BulkSmsJob, 
    FarmersLoad, FactoryCommitmentTonnage
)
from .serializers import *
from common.pagination import CustomPagination
from .serializers import FactoryCommitmentTonnageSerializer, FarmersLoadSerializer, BulkSmsJobSerializer, \
    CarriageStatusSerializer, CarriageSerializer, DriverSerializer, CarSerializer


class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    lookup_field = 'id'
    pagination_class = CustomPagination
    permission_classes = [IsAuthenticated]


class DriverViewSet(viewsets.ModelViewSet):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer
    lookup_field = 'id'
    pagination_class = CustomPagination
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['name', 'last_name', 'national_code', 'license_plate']


class CarriageViewSet(viewsets.ModelViewSet):
    queryset = Carriage.objects.all()
    serializer_class = CarriageSerializer
    lookup_field = 'id'
    pagination_class = CustomPagination
    permission_classes = [IsAuthenticated]
    filterset_fields = ['farmer', 'crop_year', 'village']


class CarriageStatusViewSet(viewsets.ModelViewSet):
    queryset = CarriageStatus.objects.all()
    serializer_class = CarriageStatusSerializer
    lookup_field = 'id'
    pagination_class = CustomPagination
    permission_classes = [IsAuthenticated]
    filterset_fields = ['carriage', 'driver']


class BulkSmsJobViewSet(viewsets.ModelViewSet):
    queryset = BulkSmsJob.objects.all()
    serializer_class = BulkSmsJobSerializer
    lookup_field = 'id'
    pagination_class = CustomPagination
    permission_classes = [IsAuthenticated]
    filterset_fields = ['status', 'job_id']


class FarmersLoadViewSet(viewsets.ModelViewSet):
    queryset = FarmersLoad.objects.all()
    serializer_class = FarmersLoadSerializer
    lookup_field = 'id'
    pagination_class = CustomPagination
    permission_classes = [IsAuthenticated]
    filterset_fields = ['farmer', 'factory', 'crop_year']
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['load_number', 'driver_name', 'phone_number']


class FactoryCommitmentTonnageViewSet(viewsets.ModelViewSet):
    queryset = FactoryCommitmentTonnage.objects.all()
    serializer_class = FactoryCommitmentTonnageSerializer
    lookup_field = 'id'
    pagination_class = CustomPagination
    permission_classes = [IsAuthenticated]
    filterset_fields = ['factory', 'crop_year']