from django.contrib import admin
print("DEBUG: config/urls.py IMPORTED")
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Baisoft Marketplace API",
      default_version='v1',
      description="Multi-tenant marketplace API",
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # API v1 Versioning
    path('api/v1/auth/', include('djoser.urls')),
    path('api/v1/auth/', include('djoser.urls.jwt')),
    path('api/v1/products/', include('apps.products.urls')),
    path('api/v1/users/', include('apps.users.urls')),
    
    # Swagger Documentation
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]

admin.site.site_header = "Baisoft Marketplace Admin"
admin.site.site_title = "Baisoft Marketplace Admin Portal"
admin.site.index_title = "Welcome to the Baisoft Marketplace Portal"
