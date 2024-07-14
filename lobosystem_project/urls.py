"""
URL configuration for lobosystem_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/app1/', include('work_orders.urls')),
    path('api/app2/', include('tasks.urls')),
    path('api/app3/', include('inventory.urls')),
    path('api/app4/', include('labor.urls')),
    path('api/app5/', include('observations.urls')),
    path('api/app6/', include('costs.urls')),
    path('api/app7/', include('files.urls')),
]
