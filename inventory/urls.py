from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PartMaterialViewSet

router = DefaultRouter()
router.register(r'parts_material', PartMaterialViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
