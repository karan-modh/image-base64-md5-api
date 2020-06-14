from django.shortcuts import render
from django.http import JsonResponse

# third party imports
from rest_framework.views import APIView
from rest_framework.response import Response


class TestView(APIView):
    def get(self, request, *args, **kwargs):
        data = {
            'base64': 'Random Shit',
            'md5': 'Encrypted Random Shit'
        }
        return Response(data)
