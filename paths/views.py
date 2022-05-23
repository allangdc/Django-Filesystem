from rest_framework import viewsets
from .models import Paths
from .serializer import PathSerializer


class PathViewSet(viewsets.ModelViewSet):
    queryset = Paths.objects.all()
    serializer_class = PathSerializer
