from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import (
    SeedViewSet, PesticideViewSet, FactorySeedViewSet, FactoryPesticideViewSet,
    FarmersSeedViewSet, FarmersPesticideViewSet, FactorySugarViewSet,
    FactoryWasteViewSet, FarmersSugarDeliveryViewSet, FarmersWasteDeliveryViewSet
)

router = DefaultRouter()

router.register(r'seed', SeedViewSet, basename='seed')
router.register(r'pesticide', PesticideViewSet, basename='pesticide')

router.register(r'factory-seed', FactorySeedViewSet, basename='factory-seed')
router.register(r'factory-pesticide', FactoryPesticideViewSet, basename='factory-pesticide')

router.register(r'farmers-seed', FarmersSeedViewSet, basename='farmers-seed')
router.register(r'farmers-pesticide', FarmersPesticideViewSet, basename='farmers-pesticide')

router.register(r'factory-sugar', FactorySugarViewSet, basename='factory-sugar')
router.register(r'factory-waste', FactoryWasteViewSet, basename='factory-waste')

router.register(r'farmers-sugar-delivery', FarmersSugarDeliveryViewSet, basename='farmers-sugar-delivery')
router.register(r'farmers-waste-delivery', FarmersWasteDeliveryViewSet, basename='farmers-waste-delivery')


urlpatterns = [
    path('', include(router.urls)),
]