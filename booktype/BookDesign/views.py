from models import BookDesign
from rest_framework import viewsets
from rest_framework.decorators import detail_route, list_route
from serializers import  BookDesignSerializer


class  BookDesignViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows  bookdesigns to be viewed or edited.
    """
    queryset =  BookDesign.objects.all()
    serializer_class =  BookDesignSerializer

