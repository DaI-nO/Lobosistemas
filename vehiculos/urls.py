from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import VehiculoViewSet, AlmacenViewSet

router = DefaultRouter()
router.register(r'tow', VehiculoViewSet)
router.register(r'warehouses', AlmacenViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
