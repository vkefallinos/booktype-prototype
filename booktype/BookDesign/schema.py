import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import graphene
from graphene import Schema, relay, resolve_only_args
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from graphene_django.debug import DjangoDebug
from booktype.BookDesign import data
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


class BookDesignNode(DjangoObjectType):
    '''A BookDesign.'''
    class Meta:
        model = models.BookDesign
        exclude_fields = ()
        filter_fields = []
        filter_order_by = ['created', 'edited']
        interfaces = (relay.Node, )

BookDesignNode.Connection = connection_for_type(BookDesignNode)


class createBookDesign(relay.ClientIDMutation):
    class Input:

        theme = graphene.String
        heading = graphene.String
        color = graphene.String
        font_size = graphene.Int
        alignment = graphene.String
        paragraph = graphene.String
        text_indent = graphene.Int
        line_height = graphene.Int

    @classmethod
    def mutate_and_get_payload(cls, input, context, info):
        theme = input.get('theme')
        heading = input.get('heading')
        color = input.get('color')
        font_size = input.get('font_size')
        alignment = input.get('alignment')
        paragraph = input.get('paragraph')
        text_indent = input.get('text_indent')
        line_height = input.get('line_height')

        bookdesign = data.create_book_design(theme, heading, color, font_size, alignment, paragraph, text_indent, line_height, )
        return createBookDesign(bookdesign)










class deleteBookDesign(relay.ClientIDMutation):
    class Input:


        bookdesign_id = graphene.ID


    @classmethod
    def mutate_and_get_payload(cls, input, context, info):
        bookdesign_id = input.get('bookdesign_id')
        return data.delete_book_design(bookdesign_id=bookdesign_id)








