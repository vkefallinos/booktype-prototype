import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import graphene
from graphene import Schema, relay, resolve_only_args
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from graphene_django.debug import DjangoDebug
from booktype.BookMetadata import data
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


class BookMetadataNode(DjangoObjectType):
    '''A BookMetadata.'''
    class Meta:
        model = models.BookMetadata
        exclude_fields = ()
        filter_fields = []
        filter_order_by = ['created', 'edited']
        interfaces = (relay.Node, )

BookMetadataNode.Connection = connection_for_type(BookMetadataNode)


class createBookMetadata(relay.ClientIDMutation):
    class Input:

        title = graphene.String
        short_title = graphene.String
        subtitle = graphene.String
        publisher = graphene.String
        publication_date = graphene.types.datetime.DateTime
        copyright_date = graphene.types.datetime.DateTime
        copyright_holder = graphene.String
        publisher_city = graphene.String
        short_description = graphene.String
        long_description = graphene.String
        ebook_isbn = graphene.String
        print_isbn = graphene.String

    @classmethod
    def mutate_and_get_payload(cls, input, context, info):
        title = input.get('title')
        short_title = input.get('short_title')
        subtitle = input.get('subtitle')
        publisher = input.get('publisher')
        publication_date = input.get('publication_date')
        copyright_date = input.get('copyright_date')
        copyright_holder = input.get('copyright_holder')
        publisher_city = input.get('publisher_city')
        short_description = input.get('short_description')
        long_description = input.get('long_description')
        ebook_isbn = input.get('ebook_isbn')
        print_isbn = input.get('print_isbn')

        bookmetadata = data.create_book_metadata(title, short_title, subtitle, publisher, publication_date, copyright_date, copyright_holder, publisher_city, short_description, long_description, ebook_isbn, print_isbn, )
        return createBookMetadata(bookmetadata)










class deleteBookMetadata(relay.ClientIDMutation):
    class Input:


        bookmetadata_id = graphene.ID


    @classmethod
    def mutate_and_get_payload(cls, input, context, info):
        bookmetadata_id = input.get('bookmetadata_id')
        return data.delete_book_metadata(bookmetadata_id=bookmetadata_id)








