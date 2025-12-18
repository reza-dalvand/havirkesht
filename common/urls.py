from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    UserViewSet, LoginView, RefreshTokenView, LogoutView, ChangePasswordView,
    UsersDashboardView, CropYearViewSet, FactoryViewSet, MeasureUnitViewSet,
    PaymentReasonViewSet
)

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='users')
router.register(r'crop-year', CropYearViewSet, basename='crop-year')
router.register(r'factory', FactoryViewSet, basename='factory')
router.register(r'measure_unit', MeasureUnitViewSet, basename='measure-unit')
router.register(r'payment-reason', PaymentReasonViewSet, basename='payment-reason')



urlpatterns = [
    path('', include(router.urls)),

    path('token/', LoginView.as_view(), name='token_obtain_pair'),
    path('refresh-token/', RefreshTokenView.as_view(), name='token_refresh'),
    path('logout', LogoutView.as_view(), name='auth_logout'),
    path('changepassword/', ChangePasswordView.as_view(), name='change-password'),

    path('users-dashboard/', UsersDashboardView.as_view(), name='users-dashboard'),
]