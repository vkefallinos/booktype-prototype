from models import Activity
from rest_framework import viewsets
from rest_framework.decorators import detail_route, list_route
from serializers import  ActivitySerializer


class  ActivityViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows  activities to be viewed or edited.
    """
    queryset =  Activity.objects.all()
    serializer_class =  ActivitySerializer

