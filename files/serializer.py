from rest_framework import serializers
from .models import Files
from paths.serializer import PathSerializer, PathSerializerFolder
import os


class FileSerializer(serializers.ModelSerializer):
    folder = PathSerializerFolder(read_only=True, source="path")
    size = serializers.SerializerMethodField("get_size")
    name = serializers.SerializerMethodField("get_name")

    def get_size(self, obj: Files):
        return obj.specs.size

    def get_name(self, obj: Files):
        return os.path.basename(obj.specs.name)

    class Meta:
        model = Files
        fields = ["id", "folder", "size", "name", "description", "specs", "path"]
        extra_kwargs = {'path': {'write_only': True}}
