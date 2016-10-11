from models import Comment
from rest_framework import viewsets
from rest_framework.decorators import detail_route, list_route
from serializers import  CommentSerializer


class  CommentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows  comments to be viewed or edited.
    """
    queryset =  Comment.objects.all()
    serializer_class =  CommentSerializer

    @detail_route(methods=['post'])
    def resolve(self, request, pk=None):
        resolved = request.data.get('resolved')
        data.resolve(comment_id=pk, resolved=resolved)







    @detail_route(methods=['post'])
    def set_user_to_book_type_user(self, request, pk=None):



        booktypeuser_id = request.data.get('booktypeuser_id')
        data.set_user_to_book_type_user(comment_id=pk, booktypeuser_id=booktypeuser_id)




    @detail_route(methods=['post'])
    def add_sub_comment_to_subcomments(self, request, pk=None):

        subcomment_id = request.data.get('subcomment_id')
        data.add_sub_comment_to_subcomments(comment_id=pk, subcomment_id=subcomment_id)






    @detail_route(methods=['post'])
    def remove_sub_comment_from_subcomments(self, request, pk=None):


        subcomment_id = request.data.get('subcomment_id')
        data.remove_sub_comment_from_subcomments(comment_id=pk, subcomment_id=subcomment_id)





    @detail_route(methods=['post'])
    def reorder_sub_comment_on_subcomments(self, request, pk=None):




        subcomment_id = request.data.get('subcomment_id')
        place = request.data.get('place')
        data.reorder_sub_comment_on_subcomments(comment_id=pk, subcomment_id=subcomment_id, place=place)



