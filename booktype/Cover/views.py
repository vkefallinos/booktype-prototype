from models import Cover
from rest_framework import viewsets
from rest_framework.decorators import detail_route, list_route
from serializers import  CoverSerializer


class  CoverViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows  covers to be viewed or edited.
    """
    queryset =  Cover.objects.all()
    serializer_class =  CoverSerializer

    @detail_route(methods=['post'])
    def approve(self, request, pk=None):
        approved = request.data.get('approved')
        data.approve(cover_id=pk, approved=approved)







