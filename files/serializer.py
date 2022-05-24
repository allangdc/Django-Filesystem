from rest_framework import serializers
from .models import Files
from paths.serializer import PathSerializer
import os


class FileSerializer(serializers.ModelSerializer):
    folder = PathSerializer(read_only=True, source="path")
    size = serializers.SerializerMethodField("get_size")
    name = serializers.SerializerMethodField("get_name")

    def get_size(self, obj: Files):
        return str(obj.specs.size)

    def get_name(self, obj: Files):
        return os.path.basename(obj.specs.name)

    class Meta:
        model = Files
        fields = ["id", "folder", "size", "name", "description", "specs"]
