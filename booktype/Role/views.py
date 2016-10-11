from models import Role
from rest_framework import viewsets
from rest_framework.decorators import detail_route, list_route
from serializers import  RoleSerializer


class  RoleViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows  roles to be viewed or edited.
    """
    queryset =  Role.objects.all()
    serializer_class =  RoleSerializer

