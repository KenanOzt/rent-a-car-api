from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from cars.views import CarViewSet

# Swagger İçin Gerekli Kütüphaneler
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Router: URL'leri otomatik oluşturur (örn: /api/cars/)
router = DefaultRouter()
router.register(r'cars', CarViewSet)

# Swagger Ayarları (Vitrin Tasarımı)
schema_view = get_schema_view(
   openapi.Info(
      title="Rent A Car API",
      default_version='v1',
      description="KenanOzt tarafindan gelistirilen Headless API projesi",
      contact=openapi.Contact(email="iletisim@example.com"),
      license=openapi.License(name="MIT License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # API Endpoint'imiz
    path('api/', include(router.urls)),
    
    # Dokümantasyon Linkleri (Ahmet'i etkileyecek kısım)
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]