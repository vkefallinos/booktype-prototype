from models import SubComment
from rest_framework import viewsets
from rest_framework.decorators import detail_route, list_route
from serializers import  SubCommentSerializer


class  SubCommentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows  subcomments to be viewed or edited.
    """
    queryset =  SubComment.objects.all()
    serializer_class =  SubCommentSerializer

    @detail_route(methods=['post'])
    def set_user_to_book_type_user(self, request, pk=None):



        booktypeuser_id = request.data.get('booktypeuser_id')
        data.set_user_to_book_type_user(subcomment_id=pk, booktypeuser_id=booktypeuser_id)




