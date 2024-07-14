from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AttachedFileViewSet

router = DefaultRouter()
router.register(r'attached_files', AttachedFileViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
