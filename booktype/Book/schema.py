import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import graphene
from graphene import Schema, relay, resolve_only_args
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from graphene_django.debug import DjangoDebug
from booktype.Book import data
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


class BookNode(DjangoObjectType):
    '''A Book.'''
    class Meta:
        model = models.Book
        exclude_fields = ()
        filter_fields = ['name', 'description', 'public', 'owner', ]
        filter_order_by = ['name', 'created', 'edited']
        interfaces = (relay.Node, )

BookNode.Connection = connection_for_type(BookNode)


class createBook(relay.ClientIDMutation):
    class Input:

        name = graphene.String
        description = graphene.String
        licence = graphene.String
        language = graphene.String
        right_to_left = graphene.Boolean
        public = graphene.Boolean
        image = graphene.String
        status = graphene.String
        created = graphene.types.datetime.DateTime
        published = graphene.types.datetime.DateTime

    @classmethod
    def mutate_and_get_payload(cls, input, context, info):
        name = input.get('name')
        description = input.get('description')
        licence = input.get('licence')
        language = input.get('language')
        right_to_left = input.get('right_to_left')
        public = input.get('public')
        image = input.get('image')
        status = input.get('status')
        created = input.get('created')
        published = input.get('published')

        book = data.create_book(name, description, licence, language, right_to_left, public, image, status, created, published, )
        return createBook(book)










class deleteBook(relay.ClientIDMutation):
    class Input:


        book_id = graphene.ID


    @classmethod
    def mutate_and_get_payload(cls, input, context, info):
        book_id = input.get('book_id')
        return data.delete_book(book_id=book_id)








class setOwnerToBookTypeUser(relay.ClientIDMutation):
    class Input:





        book_id = graphene.ID
        booktypeuser_id = graphene.ID

    @classmethod
    def mutate_and_get_payload(cls, input, context, info):
        book_id = input.get('book_id')
        booktypeuser_id = input.get('booktypeuser_id')
        return data.set_owner_to_book_type_user(book_id=book_id, booktypeuser_id=booktypeuser_id)





class setMetadataToBookMetadata(relay.ClientIDMutation):
    class Input:





        book_id = graphene.ID
        bookmetadata_id = graphene.ID

    @classmethod
    def mutate_and_get_payload(cls, input, context, info):
        book_id = input.get('book_id')
        bookmetadata_id = input.get('bookmetadata_id')
        return data.set_metadata_to_book_metadata(book_id=book_id, bookmetadata_id=bookmetadata_id)





class addRoleToRoles(relay.ClientIDMutation):
    class Input:



        book_id = graphene.ID
        role_id = graphene.ID

    @classmethod
    def mutate_and_get_payload(cls, input, context, info):
        book_id = input.get('book_id')
        role_id = input.get('role_id')
        return data.add_role_to_roles(book_id=book_id, role_id=role_id)







class removeRoleFromRoles(relay.ClientIDMutation):
    class Input:




        book_id = graphene.ID
        role_id = graphene.ID

    @classmethod
    def mutate_and_get_payload(cls, input, context, info):
        book_id = input.get('book_id')
        role_id = input.get('role_id')
        return data.remove_role_from_roles(book_id=book_id, role_id=role_id)






class reorderRoleOnRoles(relay.ClientIDMutation):
    class Input:







        book_id = graphene.ID
        role_id = graphene.ID
        place = graphene.Int

    @classmethod
    def mutate_and_get_payload(cls, input, context, info):
        book_id = input.get('book_id')
        role_id = input.get('role_id')
        place = input.get('place')
        return data.reorder_role_on_roles(book_id=book_id, role_id=role_id, place=place)



class addChapterToChapters(relay.ClientIDMutation):
    class Input:



        book_id = graphene.ID
        chapter_id = graphene.ID

    @classmethod
    def mutate_and_get_payload(cls, input, context, info):
        book_id = input.get('book_id')
        chapter_id = input.get('chapter_id')
        return data.add_chapter_to_chapters(book_id=book_id, chapter_id=chapter_id)







class removeChapterFromChapters(relay.ClientIDMutation):
    class Input:




        book_id = graphene.ID
        chapter_id = graphene.ID

    @classmethod
    def mutate_and_get_payload(cls, input, context, info):
        book_id = input.get('book_id')
        chapter_id = input.get('chapter_id')
        return data.remove_chapter_from_chapters(book_id=book_id, chapter_id=chapter_id)






class reorderChapterOnChapters(relay.ClientIDMutation):
    class Input:







        book_id = graphene.ID
        chapter_id = graphene.ID
        place = graphene.Int

    @classmethod
    def mutate_and_get_payload(cls, input, context, info):
        book_id = input.get('book_id')
        chapter_id = input.get('chapter_id')
        place = input.get('place')
        return data.reorder_chapter_on_chapters(book_id=book_id, chapter_id=chapter_id, place=place)



class addSectionToSections(relay.ClientIDMutation):
    class Input:



        book_id = graphene.ID
        section_id = graphene.ID

    @classmethod
    def mutate_and_get_payload(cls, input, context, info):
        book_id = input.get('book_id')
        section_id = input.get('section_id')
        return data.add_section_to_sections(book_id=book_id, section_id=section_id)







class removeSectionFromSections(relay.ClientIDMutation):
    class Input:




        book_id = graphene.ID
        section_id = graphene.ID

    @classmethod
    def mutate_and_get_payload(cls, input, context, info):
        book_id = input.get('book_id')
        section_id = input.get('section_id')
        return data.remove_section_from_sections(book_id=book_id, section_id=section_id)






class reorderSectionOnSections(relay.ClientIDMutation):
    class Input:







        book_id = graphene.ID
        section_id = graphene.ID
        place = graphene.Int

    @classmethod
    def mutate_and_get_payload(cls, input, context, info):
        book_id = input.get('book_id')
        section_id = input.get('section_id')
        place = input.get('place')
        return data.reorder_section_on_sections(book_id=book_id, section_id=section_id, place=place)



class addCoverToCovers(relay.ClientIDMutation):
    class Input:



        book_id = graphene.ID
        cover_id = graphene.ID

    @classmethod
    def mutate_and_get_payload(cls, input, context, info):
        book_id = input.get('book_id')
        cover_id = input.get('cover_id')
        return data.add_cover_to_covers(book_id=book_id, cover_id=cover_id)







class removeCoverFromCovers(relay.ClientIDMutation):
    class Input:




        book_id = graphene.ID
        cover_id = graphene.ID

    @classmethod
    def mutate_and_get_payload(cls, input, context, info):
        book_id = input.get('book_id')
        cover_id = input.get('cover_id')
        return data.remove_cover_from_covers(book_id=book_id, cover_id=cover_id)






class reorderCoverOnCovers(relay.ClientIDMutation):
    class Input:







        book_id = graphene.ID
        cover_id = graphene.ID
        place = graphene.Int

    @classmethod
    def mutate_and_get_payload(cls, input, context, info):
        book_id = input.get('book_id')
        cover_id = input.get('cover_id')
        place = input.get('place')
        return data.reorder_cover_on_covers(book_id=book_id, cover_id=cover_id, place=place)



class setDesignToBookDesign(relay.ClientIDMutation):
    class Input:





        book_id = graphene.ID
        bookdesign_id = graphene.ID

    @classmethod
    def mutate_and_get_payload(cls, input, context, info):
        book_id = input.get('book_id')
        bookdesign_id = input.get('bookdesign_id')
        return data.set_design_to_book_design(book_id=book_id, bookdesign_id=bookdesign_id)





