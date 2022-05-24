from rest_framework import viewsets
from .models import Files
from .serializer import FileSerializer
from django.db.models import Value, Sum


class FileViewSet(viewsets.ModelViewSet):
    queryset = Files.objects.all()
    serializer_class = FileSerializer