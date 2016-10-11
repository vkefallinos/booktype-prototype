import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import graphene
from graphene import Schema, relay, resolve_only_args
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from graphene_django.debug import DjangoDebug
from booktype.Cover import data
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


class CoverNode(DjangoObjectType):
    '''A Cover.'''
    class Meta:
        model = models.Cover
        exclude_fields = ()
        filter_fields = []
        filter_order_by = ['created', 'edited']
        interfaces = (relay.Node, )

CoverNode.Connection = connection_for_type(CoverNode)


class approve(relay.ClientIDMutation):
    class Input:








        cover_id = graphene.ID
        approved = graphene.Boolean

    @classmethod
    def mutate_and_get_payload(cls, input, context, info):
        cover_id = input.get('cover_id')
        approved = input.get('approved')
        return data.approve(cover_id=cover_id, approved=approved)


class createCover(relay.ClientIDMutation):
    class Input:

        title = graphene.String
        creator = graphene.String
        licence = graphene.String
        notes = graphene.String
        image = graphene.String
        approved = graphene.Boolean

    @classmethod
    def mutate_and_get_payload(cls, input, context, info):
        title = input.get('title')
        creator = input.get('creator')
        licence = input.get('licence')
        notes = input.get('notes')
        image = input.get('image')
        approved = input.get('approved')

        cover = data.create_cover(title, creator, licence, notes, image, approved, )
        return createCover(cover)










class deleteCover(relay.ClientIDMutation):
    class Input:


        cover_id = graphene.ID


    @classmethod
    def mutate_and_get_payload(cls, input, context, info):
        cover_id = input.get('cover_id')
        return data.delete_cover(cover_id=cover_id)








