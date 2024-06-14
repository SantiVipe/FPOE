from django.urls import path,include
from rest_framework import routers
from lavelopues.views import views

router = routers.DefaultRouter()
router.register(r'cliente', views.ClienteViewSet)
router.register(r'servicios', views.ServicioViewSet)

urlpatterns = [
    path('', include(router.urls))
]