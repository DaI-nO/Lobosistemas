from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AdditionalCostViewSet, TotalCostViewSet

router = DefaultRouter()
router.register(r'additional_costs', AdditionalCostViewSet)
router.register(r'total_costs', TotalCostViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
