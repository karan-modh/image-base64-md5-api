from rest_framework import serializers
from .models import Image
from django import forms


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['title']
