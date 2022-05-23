from rest_framework import viewsets
from .models import Files
from .serializer import FileSerializer


class FileViewSet(viewsets.ModelViewSet):
    queryset = Files.objects.all()
    serializer_class = FileSerializer

    def get_queryset(self):
        return super().get_queryset()