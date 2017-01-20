from django.conf.urls import url, include
from rest_framework import routers

from v2 import views

v2_router = routers.DefaultRouter()
v2_router.register(
    r'escenarios', views.EscenarioViewSet, base_name='Escenario'
)

urlpatterns = [
   url(r'^', include(v2_router.urls))
]
