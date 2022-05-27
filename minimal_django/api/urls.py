from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api import views

router = DefaultRouter()
router.register(r'pets', views.PetViewSet)

urlpatterns = [path('get', include(router.urls))]
