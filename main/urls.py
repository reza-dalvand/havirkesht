from django.contrib import admin
from django.urls import path, include
# from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from common import urls as common_urls
from farmer import urls as farmer_urls
from finance import urls as finance_urls
from inventory import urls as inventory_urls
from logistic import urls as logistic_urls


# تعریف ویوی شمای نهایی
schema_view = get_schema_view(
    openapi.Info(
        title="Havirkesht Backend API",
        default_version='v1',
        description="API documentation",
        # ...
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),

    path('', include(common_urls)),
    path('', include(farmer_urls)),
    path('', include(finance_urls)),
    path('', include(inventory_urls)),
    path('', include(logistic_urls)),

    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]