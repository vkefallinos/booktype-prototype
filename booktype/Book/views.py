from models import Book
from rest_framework import viewsets
from rest_framework.decorators import detail_route, list_route
from serializers import  BookSerializer


class  BookViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows  books to be viewed or edited.
    """
    queryset =  Book.objects.all()
    serializer_class =  BookSerializer

    @detail_route(methods=['post'])
    def set_owner_to_book_type_user(self, request, pk=None):



        booktypeuser_id = request.data.get('booktypeuser_id')
        data.set_owner_to_book_type_user(book_id=pk, booktypeuser_id=booktypeuser_id)




    @detail_route(methods=['post'])
    def set_metadata_to_book_metadata(self, request, pk=None):



        bookmetadata_id = request.data.get('bookmetadata_id')
        data.set_metadata_to_book_metadata(book_id=pk, bookmetadata_id=bookmetadata_id)




    @detail_route(methods=['post'])
    def add_role_to_roles(self, request, pk=None):

        role_id = request.data.get('role_id')
        data.add_role_to_roles(book_id=pk, role_id=role_id)






    @detail_route(methods=['post'])
    def remove_role_from_roles(self, request, pk=None):


        role_id = request.data.get('role_id')
        data.remove_role_from_roles(book_id=pk, role_id=role_id)





    @detail_route(methods=['post'])
    def reorder_role_on_roles(self, request, pk=None):




        role_id = request.data.get('role_id')
        place = request.data.get('place')
        data.reorder_role_on_roles(book_id=pk, role_id=role_id, place=place)



    @detail_route(methods=['post'])
    def add_chapter_to_chapters(self, request, pk=None):

        chapter_id = request.data.get('chapter_id')
        data.add_chapter_to_chapters(book_id=pk, chapter_id=chapter_id)






    @detail_route(methods=['post'])
    def remove_chapter_from_chapters(self, request, pk=None):


        chapter_id = request.data.get('chapter_id')
        data.remove_chapter_from_chapters(book_id=pk, chapter_id=chapter_id)





    @detail_route(methods=['post'])
    def reorder_chapter_on_chapters(self, request, pk=None):




        chapter_id = request.data.get('chapter_id')
        place = request.data.get('place')
        data.reorder_chapter_on_chapters(book_id=pk, chapter_id=chapter_id, place=place)



    @detail_route(methods=['post'])
    def add_section_to_sections(self, request, pk=None):

        section_id = request.data.get('section_id')
        data.add_section_to_sections(book_id=pk, section_id=section_id)






    @detail_route(methods=['post'])
    def remove_section_from_sections(self, request, pk=None):


        section_id = request.data.get('section_id')
        data.remove_section_from_sections(book_id=pk, section_id=section_id)





    @detail_route(methods=['post'])
    def reorder_section_on_sections(self, request, pk=None):




        section_id = request.data.get('section_id')
        place = request.data.get('place')
        data.reorder_section_on_sections(book_id=pk, section_id=section_id, place=place)



    @detail_route(methods=['post'])
    def add_cover_to_covers(self, request, pk=None):

        cover_id = request.data.get('cover_id')
        data.add_cover_to_covers(book_id=pk, cover_id=cover_id)






    @detail_route(methods=['post'])
    def remove_cover_from_covers(self, request, pk=None):


        cover_id = request.data.get('cover_id')
        data.remove_cover_from_covers(book_id=pk, cover_id=cover_id)





    @detail_route(methods=['post'])
    def reorder_cover_on_covers(self, request, pk=None):




        cover_id = request.data.get('cover_id')
        place = request.data.get('place')
        data.reorder_cover_on_covers(book_id=pk, cover_id=cover_id, place=place)



    @detail_route(methods=['post'])
    def set_design_to_book_design(self, request, pk=None):



        bookdesign_id = request.data.get('bookdesign_id')
        data.set_design_to_book_design(book_id=pk, bookdesign_id=bookdesign_id)




