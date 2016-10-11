import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import graphene
from graphene import Schema, relay, resolve_only_args
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from graphene_django.debug import DjangoDebug
from booktype.Comment import data
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


class CommentNode(DjangoObjectType):
    '''A Comment.'''
    class Meta:
        model = models.Comment
        exclude_fields = ()
        filter_fields = []
        filter_order_by = ['created', 'edited']
        interfaces = (relay.Node, )

CommentNode.Connection = connection_for_type(CommentNode)


class resolve(relay.ClientIDMutation):
    class Input:








        comment_id = graphene.ID
        resolved = graphene.Boolean

    @classmethod
    def mutate_and_get_payload(cls, input, context, info):
        comment_id = input.get('comment_id')
        resolved = input.get('resolved')
        return data.resolve(comment_id=comment_id, resolved=resolved)


class createComment(relay.ClientIDMutation):
    class Input:

        selected_text = graphene.String
        resolved = graphene.Boolean

    @classmethod
    def mutate_and_get_payload(cls, input, context, info):
        selected_text = input.get('selected_text')
        resolved = input.get('resolved')

        comment = data.create_comment(selected_text, resolved, )
        return createComment(comment)










class deleteComment(relay.ClientIDMutation):
    class Input:


        comment_id = graphene.ID


    @classmethod
    def mutate_and_get_payload(cls, input, context, info):
        comment_id = input.get('comment_id')
        return data.delete_comment(comment_id=comment_id)








class setUserToBookTypeUser(relay.ClientIDMutation):
    class Input:





        comment_id = graphene.ID
        booktypeuser_id = graphene.ID

    @classmethod
    def mutate_and_get_payload(cls, input, context, info):
        comment_id = input.get('comment_id')
        booktypeuser_id = input.get('booktypeuser_id')
        return data.set_user_to_book_type_user(comment_id=comment_id, booktypeuser_id=booktypeuser_id)





class addSubCommentToSubcomments(relay.ClientIDMutation):
    class Input:



        comment_id = graphene.ID
        subcomment_id = graphene.ID

    @classmethod
    def mutate_and_get_payload(cls, input, context, info):
        comment_id = input.get('comment_id')
        subcomment_id = input.get('subcomment_id')
        return data.add_sub_comment_to_subcomments(comment_id=comment_id, subcomment_id=subcomment_id)







class removeSubCommentFromSubcomments(relay.ClientIDMutation):
    class Input:




        comment_id = graphene.ID
        subcomment_id = graphene.ID

    @classmethod
    def mutate_and_get_payload(cls, input, context, info):
        comment_id = input.get('comment_id')
        subcomment_id = input.get('subcomment_id')
        return data.remove_sub_comment_from_subcomments(comment_id=comment_id, subcomment_id=subcomment_id)






class reorderSubCommentOnSubcomments(relay.ClientIDMutation):
    class Input:







        comment_id = graphene.ID
        subcomment_id = graphene.ID
        place = graphene.Int

    @classmethod
    def mutate_and_get_payload(cls, input, context, info):
        comment_id = input.get('comment_id')
        subcomment_id = input.get('subcomment_id')
        place = input.get('place')
        return data.reorder_sub_comment_on_subcomments(comment_id=comment_id, subcomment_id=subcomment_id, place=place)



