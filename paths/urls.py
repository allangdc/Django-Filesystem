from django.urls import path
from .views import PathViewSet
from rest_framework.routers import SimpleRouter

path_router = SimpleRouter()
path_router.register("", PathViewSet)