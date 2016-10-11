from models import BookMetadata
from rest_framework import viewsets
from rest_framework.decorators import detail_route, list_route
from serializers import  BookMetadataSerializer


class  BookMetadataViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows  bookmetadatas to be viewed or edited.
    """
    queryset =  BookMetadata.objects.all()
    serializer_class =  BookMetadataSerializer

