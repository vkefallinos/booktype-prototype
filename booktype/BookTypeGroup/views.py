from models import BookTypeGroup
from rest_framework import viewsets
from rest_framework.decorators import detail_route, list_route
from serializers import  BookTypeGroupSerializer


class  BookTypeGroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows  booktypegroups to be viewed or edited.
    """
    queryset =  BookTypeGroup.objects.all()
    serializer_class =  BookTypeGroupSerializer

    @detail_route(methods=['post'])
    def set_owner_to_book_type_user(self, request, pk=None):



        booktypeuser_id = request.data.get('booktypeuser_id')
        data.set_owner_to_book_type_user(booktypegroup_id=pk, booktypeuser_id=booktypeuser_id)




    @detail_route(methods=['post'])
    def add_book_type_user_to_members(self, request, pk=None):

        booktypeuser_id = request.data.get('booktypeuser_id')
        data.add_book_type_user_to_members(booktypegroup_id=pk, booktypeuser_id=booktypeuser_id)






    @detail_route(methods=['post'])
    def remove_book_type_user_from_members(self, request, pk=None):


        booktypeuser_id = request.data.get('booktypeuser_id')
        data.remove_book_type_user_from_members(booktypegroup_id=pk, booktypeuser_id=booktypeuser_id)





    @detail_route(methods=['post'])
    def reorder_book_type_user_on_members(self, request, pk=None):




        booktypeuser_id = request.data.get('booktypeuser_id')
        place = request.data.get('place')
        data.reorder_book_type_user_on_members(booktypegroup_id=pk, booktypeuser_id=booktypeuser_id, place=place)



    @detail_route(methods=['post'])
    def add_book_to_books(self, request, pk=None):

        book_id = request.data.get('book_id')
        data.add_book_to_books(booktypegroup_id=pk, book_id=book_id)






    @detail_route(methods=['post'])
    def remove_book_from_books(self, request, pk=None):


        book_id = request.data.get('book_id')
        data.remove_book_from_books(booktypegroup_id=pk, book_id=book_id)





    @detail_route(methods=['post'])
    def reorder_book_on_books(self, request, pk=None):




        book_id = request.data.get('book_id')
        place = request.data.get('place')
        data.reorder_book_on_books(booktypegroup_id=pk, book_id=book_id, place=place)



