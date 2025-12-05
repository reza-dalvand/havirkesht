from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import (
    PurityPriceViewSet, ProductPriceViewSet, FarmersPaymentViewSet,
    FarmersInvoicePayedViewSet, FarmersGuaranteeViewSet, FactoryPaymentViewSet
)

router = DefaultRouter()

router.register(r'purity-price', PurityPriceViewSet, basename='purity-price')
router.register(r'product-price', ProductPriceViewSet, basename='product-price')
router.register(r'farmers-payment', FarmersPaymentViewSet, basename='farmers-payment')
router.register(r'farmers-invoice-payed', FarmersInvoicePayedViewSet, basename='farmers-invoice-payed')
router.register(r'farmers-guarantee', FarmersGuaranteeViewSet, basename='farmers-guarantee')
router.register(r'factory-payment', FactoryPaymentViewSet, basename='factory-payment')

urlpatterns = [
    path('', include(router.urls)),
]