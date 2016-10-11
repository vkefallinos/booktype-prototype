from models import Chapter
from rest_framework import viewsets
from rest_framework.decorators import detail_route, list_route
from serializers import  ChapterSerializer


class  ChapterViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows  chapters to be viewed or edited.
    """
    queryset =  Chapter.objects.all()
    serializer_class =  ChapterSerializer

    @detail_route(methods=['post'])
    def add_comment_to_comments(self, request, pk=None):

        comment_id = request.data.get('comment_id')
        data.add_comment_to_comments(chapter_id=pk, comment_id=comment_id)






    @detail_route(methods=['post'])
    def remove_comment_from_comments(self, request, pk=None):


        comment_id = request.data.get('comment_id')
        data.remove_comment_from_comments(chapter_id=pk, comment_id=comment_id)





    @detail_route(methods=['post'])
    def reorder_comment_on_comments(self, request, pk=None):




        comment_id = request.data.get('comment_id')
        place = request.data.get('place')
        data.reorder_comment_on_comments(chapter_id=pk, comment_id=comment_id, place=place)



