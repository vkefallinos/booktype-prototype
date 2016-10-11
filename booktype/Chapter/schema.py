import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import graphene
from graphene import Schema, relay, resolve_only_args
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from graphene_django.debug import DjangoDebug
from booktype.Chapter import data
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


class ChapterNode(DjangoObjectType):
    '''A Chapter.'''
    class Meta:
        model = models.Chapter
        exclude_fields = ()
        filter_fields = []
        filter_order_by = ['created', 'edited']
        interfaces = (relay.Node, )

ChapterNode.Connection = connection_for_type(ChapterNode)


class createChapter(relay.ClientIDMutation):
    class Input:

        title = graphene.String
        content = graphene.String
        status = graphene.String

    @classmethod
    def mutate_and_get_payload(cls, input, context, info):
        title = input.get('title')
        content = input.get('content')
        status = input.get('status')

        chapter = data.create_chapter(title, content, status, )
        return createChapter(chapter)










class deleteChapter(relay.ClientIDMutation):
    class Input:


        chapter_id = graphene.ID


    @classmethod
    def mutate_and_get_payload(cls, input, context, info):
        chapter_id = input.get('chapter_id')
        return data.delete_chapter(chapter_id=chapter_id)








class addCommentToComments(relay.ClientIDMutation):
    class Input:



        chapter_id = graphene.ID
        comment_id = graphene.ID

    @classmethod
    def mutate_and_get_payload(cls, input, context, info):
        chapter_id = input.get('chapter_id')
        comment_id = input.get('comment_id')
        return data.add_comment_to_comments(chapter_id=chapter_id, comment_id=comment_id)







class removeCommentFromComments(relay.ClientIDMutation):
    class Input:




        chapter_id = graphene.ID
        comment_id = graphene.ID

    @classmethod
    def mutate_and_get_payload(cls, input, context, info):
        chapter_id = input.get('chapter_id')
        comment_id = input.get('comment_id')
        return data.remove_comment_from_comments(chapter_id=chapter_id, comment_id=comment_id)






class reorderCommentOnComments(relay.ClientIDMutation):
    class Input:







        chapter_id = graphene.ID
        comment_id = graphene.ID
        place = graphene.Int

    @classmethod
    def mutate_and_get_payload(cls, input, context, info):
        chapter_id = input.get('chapter_id')
        comment_id = input.get('comment_id')
        place = input.get('place')
        return data.reorder_comment_on_comments(chapter_id=chapter_id, comment_id=comment_id, place=place)



