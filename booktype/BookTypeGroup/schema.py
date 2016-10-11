import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import graphene
from graphene import Schema, relay, resolve_only_args
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from graphene_django.debug import DjangoDebug
from booktype.BookTypeGroup import data
import models


def connection_for_type(_type):
    class Connection(graphene.Connection):
        total_count = graphene.Int()

        class Meta:
            name = _type._meta.name + 'Connection'
            node = _type

        def resolve_total_count(self, args, context, info):
            return self.length

    return Connection


class BookTypeGroupNode(DjangoObjectType):
    '''A BookTypeGroup.'''
    class Meta:
        model = models.BookTypeGroup
        exclude_fields = ()
        filter_fields = []
        filter_order_by = ['created', 'edited']
        interfaces = (relay.Node, )

BookTypeGroupNode.Connection = connection_for_type(BookTypeGroupNode)


class createBookTypeGroup(relay.ClientIDMutation):
    class Input:

        name = graphene.String
        description = graphene.String
        image = graphene.String

    @classmethod
    def mutate_and_get_payload(cls, input, context, info):
        name = input.get('name')
        description = input.get('description')
        image = input.get('image')

        booktypegroup = data.create_book_type_group(name, description, image, )
        return createBookTypeGroup(booktypegroup)










class deleteBookTypeGroup(relay.ClientIDMutation):
    class Input:


        booktypegroup_id = graphene.ID


    @classmethod
    def mutate_and_get_payload(cls, input, context, info):
        booktypegroup_id = input.get('booktypegroup_id')
        return data.delete_book_type_group(booktypegroup_id=booktypegroup_id)








class setOwnerToBookTypeUser(relay.ClientIDMutation):
    class Input:





        booktypegroup_id = graphene.ID
        booktypeuser_id = graphene.ID

    @classmethod
    def mutate_and_get_payload(cls, input, context, info):
        booktypegroup_id = input.get('booktypegroup_id')
        booktypeuser_id = input.get('booktypeuser_id')
        return data.set_owner_to_book_type_user(booktypegroup_id=booktypegroup_id, booktypeuser_id=booktypeuser_id)





class addBookTypeUserToMembers(relay.ClientIDMutation):
    class Input:



        booktypegroup_id = graphene.ID
        booktypeuser_id = graphene.ID

    @classmethod
    def mutate_and_get_payload(cls, input, context, info):
        booktypegroup_id = input.get('booktypegroup_id')
        booktypeuser_id = input.get('booktypeuser_id')
        return data.add_book_type_user_to_members(booktypegroup_id=booktypegroup_id, booktypeuser_id=booktypeuser_id)







class removeBookTypeUserFromMembers(relay.ClientIDMutation):
    class Input:




        booktypegroup_id = graphene.ID
        booktypeuser_id = graphene.ID

    @classmethod
    def mutate_and_get_payload(cls, input, context, info):
        booktypegroup_id = input.get('booktypegroup_id')
        booktypeuser_id = input.get('booktypeuser_id')
        return data.remove_book_type_user_from_members(booktypegroup_id=booktypegroup_id, booktypeuser_id=booktypeuser_id)






class reorderBookTypeUserOnMembers(relay.ClientIDMutation):
    class Input:







        booktypegroup_id = graphene.ID
        booktypeuser_id = graphene.ID
        place = graphene.Int

    @classmethod
    def mutate_and_get_payload(cls, input, context, info):
        booktypegroup_id = input.get('booktypegroup_id')
        booktypeuser_id = input.get('booktypeuser_id')
        place = input.get('place')
        return data.reorder_book_type_user_on_members(booktypegroup_id=booktypegroup_id, booktypeuser_id=booktypeuser_id, place=place)



class addBookToBooks(relay.ClientIDMutation):
    class Input:



        booktypegroup_id = graphene.ID
        book_id = graphene.ID

    @classmethod
    def mutate_and_get_payload(cls, input, context, info):
        booktypegroup_id = input.get('booktypegroup_id')
        book_id = input.get('book_id')
        return data.add_book_to_books(booktypegroup_id=booktypegroup_id, book_id=book_id)







class removeBookFromBooks(relay.ClientIDMutation):
    class Input:




        booktypegroup_id = graphene.ID
        book_id = graphene.ID

    @classmethod
    def mutate_and_get_payload(cls, input, context, info):
        booktypegroup_id = input.get('booktypegroup_id')
        book_id = input.get('book_id')
        return data.remove_book_from_books(booktypegroup_id=booktypegroup_id, book_id=book_id)






class reorderBookOnBooks(relay.ClientIDMutation):
    class Input:







        booktypegroup_id = graphene.ID
        book_id = graphene.ID
        place = graphene.Int

    @classmethod
    def mutate_and_get_payload(cls, input, context, info):
        booktypegroup_id = input.get('booktypegroup_id')
        book_id = input.get('book_id')
        place = input.get('place')
        return data.reorder_book_on_books(booktypegroup_id=booktypegroup_id, book_id=book_id, place=place)



