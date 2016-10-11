import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import graphene
from graphene import Schema, relay, resolve_only_args
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from graphene_django.debug import DjangoDebug
from booktype.Activity import data
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


class ActivityNode(DjangoObjectType):
    '''A Activity.'''
    class Meta:
        model = models.Activity
        exclude_fields = ()
        filter_fields = []
        filter_order_by = ['created', 'edited']
        interfaces = (relay.Node, )

ActivityNode.Connection = connection_for_type(ActivityNode)


class createActivity(relay.ClientIDMutation):
    class Input:

        action = graphene.String
        revision = graphene.Float

    @classmethod
    def mutate_and_get_payload(cls, input, context, info):
        action = input.get('action')
        revision = input.get('revision')

        activity = data.create_activity(action, revision, )
        return createActivity(activity)










class deleteActivity(relay.ClientIDMutation):
    class Input:


        activity_id = graphene.ID


    @classmethod
    def mutate_and_get_payload(cls, input, context, info):
        activity_id = input.get('activity_id')
        return data.delete_activity(activity_id=activity_id)








