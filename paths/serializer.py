from rest_framework import serializers
from .models import Paths

class PathSerializer(serializers.ModelSerializer):
    pathname = serializers.SerializerMethodField("get_pathname")

    def get_pathname(self, obj: Paths):
        return str(obj)

    class Meta:
        model = Paths
        fields = "__all__"


class PathSerializerFolder(serializers.ModelSerializer):
    pathname = serializers.SerializerMethodField("get_pathname")

    def get_pathname(self, obj: Paths):
        return str(obj)

    class Meta:
        model = Paths
        fields = ["pathname"]