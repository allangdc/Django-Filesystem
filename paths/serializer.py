from rest_framework import serializers
from .models import Paths


class PathSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paths
        fields = "__all__"