from models import BookTypeUser
from rest_framework import viewsets
from rest_framework.decorators import detail_route, list_route
from serializers import  BookTypeUserSerializer


class  BookTypeUserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows  booktypeusers to be viewed or edited.
    """
    queryset =  BookTypeUser.objects.all()
    serializer_class =  BookTypeUserSerializer

