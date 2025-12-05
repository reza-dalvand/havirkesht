from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Province, City, Village, Farmer, Supervisor, Commitment
from .serializers import (
    ProvinceSerializer, CitySerializer, VillageSerializer, FarmerSerializer,
    SupervisorSerializer, CommitmentSerializer
)
from common.pagination import CustomPagination


class ProvinceViewSet(viewsets.ModelViewSet):
    queryset = Province.objects.all()
    serializer_class = ProvinceSerializer
    lookup_field = 'id'
    pagination_class = CustomPagination
    permission_classes = [IsAuthenticated]


class CityViewSet(viewsets.ModelViewSet):
    """مدیریت عملیات CRUD برای شهرها (/city/)"""
    queryset = City.objects.all()
    serializer_class = CitySerializer
    lookup_field = 'id'
    pagination_class = CustomPagination
    permission_classes = [IsAuthenticated]


class VillageViewSet(viewsets.ModelViewSet):
    queryset = Village.objects.all()
    serializer_class = VillageSerializer
    lookup_field = 'id'
    pagination_class = CustomPagination
    permission_classes = [IsAuthenticated]


class FarmerViewSet(viewsets.ModelViewSet):
    queryset = Farmer.objects.all()
    serializer_class = FarmerSerializer
    lookup_field = 'id'
    pagination_class = CustomPagination
    permission_classes = [IsAuthenticated]


class SupervisorViewSet(viewsets.ModelViewSet):
    queryset = Supervisor.objects.all()
    serializer_class = SupervisorSerializer
    lookup_field = 'id'
    pagination_class = CustomPagination
    permission_classes = [IsAuthenticated]


class CommitmentViewSet(viewsets.ModelViewSet):
    queryset = Commitment.objects.all()
    serializer_class = CommitmentSerializer
    lookup_field = 'id'
    pagination_class = CustomPagination
    permission_classes = [IsAuthenticated]
    filterset_fields = ['farmer', 'crop_year']