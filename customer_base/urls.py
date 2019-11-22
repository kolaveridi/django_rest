"""customer_base URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path,include
from rest_framework import routers, serializers, viewsets
from core.views import CustomerViewSet, ProfessionViewSet,DataSheetViewSet ,DocumentViewSet


router = routers.DefaultRouter()
router.register(r'customers', CustomerViewSet)
router.register(r'professions',ProfessionViewSet)
router.register(r'data-sheet', DataSheetViewSet)
router.register(r'documents', DocumentViewSet)


urlpatterns = [
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls'))
]
