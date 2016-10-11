import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import graphene
from graphene import Schema, relay, resolve_only_args
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from graphene_django.debug import DjangoDebug
from booktype.Section import data
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


class SectionNode(DjangoObjectType):
    '''A Section.'''
    class Meta:
        model = models.Section
        exclude_fields = ()
        filter_fields = []
        filter_order_by = ['created', 'edited']
        interfaces = (relay.Node, )

SectionNode.Connection = connection_for_type(SectionNode)


class createSection(relay.ClientIDMutation):
    class Input:

        title = graphene.String

    @classmethod
    def mutate_and_get_payload(cls, input, context, info):
        title = input.get('title')

        section = data.create_section(title, )
        return createSection(section)










class deleteSection(relay.ClientIDMutation):
    class Input:


        section_id = graphene.ID


    @classmethod
    def mutate_and_get_payload(cls, input, context, info):
        section_id = input.get('section_id')
        return data.delete_section(section_id=section_id)








class addChapterToChapters(relay.ClientIDMutation):
    class Input:



        section_id = graphene.ID
        chapter_id = graphene.ID

    @classmethod
    def mutate_and_get_payload(cls, input, context, info):
        section_id = input.get('section_id')
        chapter_id = input.get('chapter_id')
        return data.add_chapter_to_chapters(section_id=section_id, chapter_id=chapter_id)







class removeChapterFromChapters(relay.ClientIDMutation):
    class Input:




        section_id = graphene.ID
        chapter_id = graphene.ID

    @classmethod
    def mutate_and_get_payload(cls, input, context, info):
        section_id = input.get('section_id')
        chapter_id = input.get('chapter_id')
        return data.remove_chapter_from_chapters(section_id=section_id, chapter_id=chapter_id)






class reorderChapterOnChapters(relay.ClientIDMutation):
    class Input:







        section_id = graphene.ID
        chapter_id = graphene.ID
        place = graphene.Int

    @classmethod
    def mutate_and_get_payload(cls, input, context, info):
        section_id = input.get('section_id')
        chapter_id = input.get('chapter_id')
        place = input.get('place')
        return data.reorder_chapter_on_chapters(section_id=section_id, chapter_id=chapter_id, place=place)



