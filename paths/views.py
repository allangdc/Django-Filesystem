from rest_framework import viewsets
from django.db.models import Q
from .models import Paths
from files.models import Files
from .serializer import PathSerializer
from files.serializer import FileSerializer
from rest_framework.decorators import action
from rest_framework.response import Response


class PathViewSet(viewsets.ModelViewSet):
    queryset = Paths.objects.all()
    serializer_class = PathSerializer

    @action(detail=True, methods=["get"])
    def listfiles(self, request, pk=None):
        path = self.get_object()
        print("AQUI 1")
        serializer = FileSerializer(path.files.all(), many=True)
        print("AQUI 2")
        return Response(serializer.data)

    @action(detail=True, methods=["get"])
    def listpaths(self, request, pk=None):
        path = self.get_object()
        print("AQUI 1")
        serializer = PathSerializer(path.paths.filter(~Q(path="/")), many=True)
        print("AQUI 2")
        return Response(serializer.data)