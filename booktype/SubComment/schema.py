import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import graphene
from graphene import Schema, relay, resolve_only_args
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from graphene_django.debug import DjangoDebug
from booktype.SubComment import data
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


class SubCommentNode(DjangoObjectType):
    '''A SubComment.'''
    class Meta:
        model = models.SubComment
        exclude_fields = ()
        filter_fields = []
        filter_order_by = ['created', 'edited']
        interfaces = (relay.Node, )

SubCommentNode.Connection = connection_for_type(SubCommentNode)


class createSubComment(relay.ClientIDMutation):
    class Input:

        text = graphene.String

    @classmethod
    def mutate_and_get_payload(cls, input, context, info):
        text = input.get('text')

        subcomment = data.create_sub_comment(text, )
        return createSubComment(subcomment)










class deleteSubComment(relay.ClientIDMutation):
    class Input:


        subcomment_id = graphene.ID


    @classmethod
    def mutate_and_get_payload(cls, input, context, info):
        subcomment_id = input.get('subcomment_id')
        return data.delete_sub_comment(subcomment_id=subcomment_id)








class setUserToBookTypeUser(relay.ClientIDMutation):
    class Input:





        subcomment_id = graphene.ID
        booktypeuser_id = graphene.ID

    @classmethod
    def mutate_and_get_payload(cls, input, context, info):
        subcomment_id = input.get('subcomment_id')
        booktypeuser_id = input.get('booktypeuser_id')
        return data.set_user_to_book_type_user(subcomment_id=subcomment_id, booktypeuser_id=booktypeuser_id)





