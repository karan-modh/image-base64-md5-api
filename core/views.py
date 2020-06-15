import base64
from .models import Image
from .serializers import ImageSerializer

# third party imports
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser


class FileUploadView(APIView):
    parser_classes = (MultiPartParser, )

    def get(self, request, *args, **kwargs):
        queryset = Image.objects.all()
        serializer = ImageSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = ImageSerializer(data=request.data)
        base64string = base64.b64encode(request.data['file'].read())
        print("-------------------\n")
        print(base64string)
        print("\n-------------------\n")
        # print(serializer.initial_data['file'])
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
