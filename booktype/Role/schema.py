import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import graphene
from graphene import Schema, relay, resolve_only_args
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from graphene_django.debug import DjangoDebug
from booktype.Role import data
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


class RoleNode(DjangoObjectType):
    '''A Role.'''
    class Meta:
        model = models.Role
        exclude_fields = ()
        filter_fields = []
        filter_order_by = ['created', 'edited']
        interfaces = (relay.Node, )

RoleNode.Connection = connection_for_type(RoleNode)


class createRole(relay.ClientIDMutation):
    class Input:

        name = graphene.String
        description = graphene.String

    @classmethod
    def mutate_and_get_payload(cls, input, context, info):
        name = input.get('name')
        description = input.get('description')

        role = data.create_role(name, description, )
        return createRole(role)










class deleteRole(relay.ClientIDMutation):
    class Input:


        role_id = graphene.ID


    @classmethod
    def mutate_and_get_payload(cls, input, context, info):
        role_id = input.get('role_id')
        return data.delete_role(role_id=role_id)








