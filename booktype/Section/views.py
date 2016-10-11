from models import Section
from rest_framework import viewsets
from rest_framework.decorators import detail_route, list_route
from serializers import  SectionSerializer


class  SectionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows  sections to be viewed or edited.
    """
    queryset =  Section.objects.all()
    serializer_class =  SectionSerializer

    @detail_route(methods=['post'])
    def add_chapter_to_chapters(self, request, pk=None):

        chapter_id = request.data.get('chapter_id')
        data.add_chapter_to_chapters(section_id=pk, chapter_id=chapter_id)






    @detail_route(methods=['post'])
    def remove_chapter_from_chapters(self, request, pk=None):


        chapter_id = request.data.get('chapter_id')
        data.remove_chapter_from_chapters(section_id=pk, chapter_id=chapter_id)





    @detail_route(methods=['post'])
    def reorder_chapter_on_chapters(self, request, pk=None):




        chapter_id = request.data.get('chapter_id')
        place = request.data.get('place')
        data.reorder_chapter_on_chapters(section_id=pk, chapter_id=chapter_id, place=place)



