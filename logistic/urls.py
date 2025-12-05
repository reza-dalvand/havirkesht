# logistics/urls.py

from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import (
    CarViewSet, DriverViewSet, CarriageViewSet, CarriageStatusViewSet,
    BulkSmsJobViewSet, FarmersLoadViewSet, FactoryCommitmentTonnageViewSet
)

router = DefaultRouter()

router.register(r'car', CarViewSet, basename='car')
router.register(r'driver', DriverViewSet, basename='driver')

router.register(r'carriage', CarriageViewSet, basename='carriage')
router.register(r'carriage-status', CarriageStatusViewSet, basename='carriage-status')

router.register(r'farmers-load', FarmersLoadViewSet, basename='farmers-load')
router.register(r'factory-commitment-tonnage', FactoryCommitmentTonnageViewSet, basename='factory-commitment-tonnage')

router.register(r'bulk-sms-job', BulkSmsJobViewSet, basename='bulk-sms-job')


urlpatterns = [
    path('', include(router.urls)),
]