import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import graphene
from graphene import Schema, relay, resolve_only_args
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from graphene_django.debug import DjangoDebug
from booktype.BookStatus import data
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


class BookStatusNode(DjangoObjectType):
    '''A BookStatus.'''
    class Meta:
        model = models.BookStatus
        exclude_fields = ()
        filter_fields = []
        filter_order_by = ['created', 'edited']
        interfaces = (relay.Node, )

BookStatusNode.Connection = connection_for_type(BookStatusNode)


class createBookStatus(relay.ClientIDMutation):
    class Input:

        status = graphene.String

    @classmethod
    def mutate_and_get_payload(cls, input, context, info):
        status = input.get('status')

        bookstatus = data.create_book_status(status, )
        return createBookStatus(bookstatus)










class deleteBookStatus(relay.ClientIDMutation):
    class Input:


        bookstatus_id = graphene.ID


    @classmethod
    def mutate_and_get_payload(cls, input, context, info):
        bookstatus_id = input.get('bookstatus_id')
        return data.delete_book_status(bookstatus_id=bookstatus_id)








