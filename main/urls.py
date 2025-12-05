from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView

from common import urls as common_urls
from farmer import urls as farmer_urls
from finance import urls as finance_urls
from inventory import urls as inventory_urls
from logistic import urls as logistic_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),

    path('api/v1/', include(common_urls)),
    path('api/v1/', include(farmer_urls)),
    path('api/v1/', include(finance_urls)),
    path('api/v1/', include(inventory_urls)),
    path('api/v1/', include(logistic_urls)),

    path('api/v1/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/v1/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/v1/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),

]