import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import graphene
from graphene import Schema, relay, resolve_only_args
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from graphene_django.debug import DjangoDebug
from booktype.BookTypeUser import data
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


class BookTypeUserNode(DjangoObjectType):
    '''A BookTypeUser.'''
    class Meta:
        model = models.BookTypeUser
        exclude_fields = ()
        filter_fields = []
        filter_order_by = ['created', 'edited']
        interfaces = (relay.Node, )

BookTypeUserNode.Connection = connection_for_type(BookTypeUserNode)


class createBookTypeUser(relay.ClientIDMutation):
    class Input:

        email = graphene.String
        fullName = graphene.String
        about = graphene.String
        profile_image = graphene.String
        public_email = graphene.String
        twitter = graphene.String
        facebook = graphene.String
        linked_in = graphene.String
        youtube = graphene.String
        vimeo = graphene.String
        hashed_password = graphene.String
        preferred_Language = graphene.String

    @classmethod
    def mutate_and_get_payload(cls, input, context, info):
        email = input.get('email')
        fullName = input.get('fullName')
        about = input.get('about')
        profile_image = input.get('profile_image')
        public_email = input.get('public_email')
        twitter = input.get('twitter')
        facebook = input.get('facebook')
        linked_in = input.get('linked_in')
        youtube = input.get('youtube')
        vimeo = input.get('vimeo')
        hashed_password = input.get('hashed_password')
        preferred_Language = input.get('preferred_Language')

        booktypeuser = data.create_book_type_user(email, fullName, about, profile_image, public_email, twitter, facebook, linked_in, youtube, vimeo, hashed_password, preferred_Language, )
        return createBookTypeUser(booktypeuser)










class deleteBookTypeUser(relay.ClientIDMutation):
    class Input:


        booktypeuser_id = graphene.ID


    @classmethod
    def mutate_and_get_payload(cls, input, context, info):
        booktypeuser_id = input.get('booktypeuser_id')
        return data.delete_book_type_user(booktypeuser_id=booktypeuser_id)








