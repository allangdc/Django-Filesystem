from django.urls import path
from .views import FileViewSet
from rest_framework.routers import SimpleRouter

file_router = SimpleRouter()
file_router.register("", FileViewSet)