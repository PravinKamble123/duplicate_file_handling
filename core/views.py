from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import File
from .serializer import FileSerializer
from .utils import check_file_name_exists_or_not


@api_view(['post'])
def create_file(request):
    serializer = FileSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    
@api_view(['get'])
def get_files(request):
    try:
        files = File.objects.all()
    except File.DoesNotExist:
        return Response({"error":"files don't exists"}, status=status.HTTP_404_NOT_FOUND)
    serializer = FileSerializer(files, many=True)
    return Response(serializer.data, status= status.HTTP_200_OK)

