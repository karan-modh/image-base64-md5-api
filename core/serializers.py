from rest_framework import serializers
from .models import Image


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = "__all__"


class InputImageSerializer(serializers.Serializer):
    file = serializers.FileField()
