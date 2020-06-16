# Functional Imports
import base64
import hashlib

# third party imports
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer, JSONRenderer
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
    # renderer_classes = [JSONRenderer]

    def post(self, request, *args, **kwargs):
        serializer = ImageSerializer(data=request.data)
        if len(request.FILES) == 0:
            return Response({'detail': 'No file selected'}, status=status.HTTP_204_NO_CONTENT)
        uploaded_file = request.FILES['file']
        file_type = uploaded_file.content_type.split('/')[0]
        if file_type != "image":
            return Response({'detail': 'Only image file types are allowed'}, status=status.HTTP_400_BAD_REQUEST)
        base64string = base64.b64encode(request.FILES['file'].read())
        md5hash = hashlib.md5(base64string)
        if serializer.is_valid():
            serializer.save()
            Image.objects.order_by('-id')[0].delete()
            return Response({'base64': base64string, 'md5': md5hash.hexdigest()}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
