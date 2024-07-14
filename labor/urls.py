from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LaborDetailViewSet

router = DefaultRouter()
router.register(r'labor_details', LaborDetailViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
