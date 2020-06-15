# Functional Imports
import base64
import hashlib

# third party imports
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.parsers import MultiPartParser

# Project Imports
from .models import Image
from .serializers import ImageSerializer


class FormDisplayView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'upload_file.html'

    def get(self, request, *args, **kwargs):
        serializer = ImageSerializer()
        return Response({'serializer': serializer})


class FileUploadView(APIView):
    parser_classes = (MultiPartParser, )

    # def get(self, request, *args, **kwargs):
    #     queryset = Image.objects.all()
    #     serializer = ImageSerializer(queryset, many=True)
    #     return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = ImageSerializer(data=request.data)
        base64string = base64.b64encode(request.FILES['file'].read())
        md5hash = hashlib.md5(base64string)
        if serializer.is_valid():
            serializer.save()
            return Response({'base64': base64string, 'md5': md5hash.hexdigest()}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
