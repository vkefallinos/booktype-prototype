from models import BookStatus
from rest_framework import viewsets
from rest_framework.decorators import detail_route, list_route
from serializers import  BookStatusSerializer


class  BookStatusViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows  bookstatuses to be viewed or edited.
    """
    queryset =  BookStatus.objects.all()
    serializer_class =  BookStatusSerializer

