from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import WorkOrderViewSet, OrdenTrabajoViewSet

router = DefaultRouter()
router.register(r'work_orders', WorkOrderViewSet)
router.register(r'ordenes-trabajo', OrdenTrabajoViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
