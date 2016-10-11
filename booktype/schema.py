from booktype.BookTypeUser.schema import BookTypeUserNode, createBookTypeUser, deleteBookTypeUser
from booktype.BookTypeGroup.schema import BookTypeGroupNode, createBookTypeGroup, deleteBookTypeGroup, setOwnerToBookTypeUser, addBookTypeUserToMembers, removeBookTypeUserFromMembers, reorderBookTypeUserOnMembers, addBookToBooks, removeBookFromBooks, reorderBookOnBooks
from booktype.Book.schema import BookNode, createBook, deleteBook, setOwnerToBookTypeUser, setMetadataToBookMetadata, addRoleToRoles, removeRoleFromRoles, reorderRoleOnRoles, addChapterToChapters, removeChapterFromChapters, reorderChapterOnChapters, addSectionToSections, removeSectionFromSections, reorderSectionOnSections, addCoverToCovers, removeCoverFromCovers, reorderCoverOnCovers, setDesignToBookDesign
from booktype.BookDesign.schema import BookDesignNode, createBookDesign, deleteBookDesign
from booktype.Cover.schema import CoverNode, approve, createCover, deleteCover
from booktype.Section.schema import SectionNode, createSection, deleteSection, addChapterToChapters, removeChapterFromChapters, reorderChapterOnChapters
from booktype.Chapter.schema import ChapterNode, createChapter, deleteChapter, addCommentToComments, removeCommentFromComments, reorderCommentOnComments
from booktype.Comment.schema import CommentNode, resolve, createComment, deleteComment, setUserToBookTypeUser, addSubCommentToSubcomments, removeSubCommentFromSubcomments, reorderSubCommentOnSubcomments
from booktype.SubComment.schema import SubCommentNode, createSubComment, deleteSubComment, setUserToBookTypeUser
from booktype.BookStatus.schema import BookStatusNode, createBookStatus, deleteBookStatus
from booktype.BookMetadata.schema import BookMetadataNode, createBookMetadata, deleteBookMetadata
from booktype.Role.schema import RoleNode, createRole, deleteRole
from booktype.Activity.schema import ActivityNode, createActivity, deleteActivity

import graphene
from graphene import ObjectType, Field
from graphene_django.filter import DjangoFilterConnectionField



class Query(ObjectType):

    booktypeuser = Field(BookTypeUserNode)
    all_BookTypeUsers = DjangoFilterConnectionField(BookTypeUserNode)


    booktypegroup = Field(BookTypeGroupNode)
    all_BookTypeGroups = DjangoFilterConnectionField(BookTypeGroupNode)


    book = Field(BookNode)
    all_Books = DjangoFilterConnectionField(BookNode)


    bookdesign = Field(BookDesignNode)
    all_BookDesigns = DjangoFilterConnectionField(BookDesignNode)


    cover = Field(CoverNode)
    all_Covers = DjangoFilterConnectionField(CoverNode)


    section = Field(SectionNode)
    all_Sections = DjangoFilterConnectionField(SectionNode)


    chapter = Field(ChapterNode)
    all_Chapters = DjangoFilterConnectionField(ChapterNode)


    comment = Field(CommentNode)
    all_Comments = DjangoFilterConnectionField(CommentNode)


    subcomment = Field(SubCommentNode)
    all_SubComments = DjangoFilterConnectionField(SubCommentNode)


    bookstatus = Field(BookStatusNode)
    all_BookStatuses = DjangoFilterConnectionField(BookStatusNode)


    bookmetadata = Field(BookMetadataNode)
    all_BookMetadatas = DjangoFilterConnectionField(BookMetadataNode)


    role = Field(RoleNode)
    all_Roles = DjangoFilterConnectionField(RoleNode)


    activity = Field(ActivityNode)
    all_Activities = DjangoFilterConnectionField(ActivityNode)




class Mutation(graphene.ObjectType):
    createbooktypeuser = createBookTypeUser.Field()
    deletebooktypeuser = deleteBookTypeUser.Field()


    createbooktypegroup = createBookTypeGroup.Field()
    deletebooktypegroup = deleteBookTypeGroup.Field()
    setownertobooktypeuser = setOwnerToBookTypeUser.Field()
    addbooktypeusertomembers = addBookTypeUserToMembers.Field()
    removebooktypeuserfrommembers = removeBookTypeUserFromMembers.Field()
    reorderbooktypeuseronmembers = reorderBookTypeUserOnMembers.Field()
    addbooktobooks = addBookToBooks.Field()
    removebookfrombooks = removeBookFromBooks.Field()
    reorderbookonbooks = reorderBookOnBooks.Field()


    createbook = createBook.Field()
    deletebook = deleteBook.Field()
    setownertobooktypeuser = setOwnerToBookTypeUser.Field()
    setmetadatatobookmetadata = setMetadataToBookMetadata.Field()
    addroletoroles = addRoleToRoles.Field()
    removerolefromroles = removeRoleFromRoles.Field()
    reorderroleonroles = reorderRoleOnRoles.Field()
    addchaptertochapters = addChapterToChapters.Field()
    removechapterfromchapters = removeChapterFromChapters.Field()
    reorderchapteronchapters = reorderChapterOnChapters.Field()
    addsectiontosections = addSectionToSections.Field()
    removesectionfromsections = removeSectionFromSections.Field()
    reordersectiononsections = reorderSectionOnSections.Field()
    addcovertocovers = addCoverToCovers.Field()
    removecoverfromcovers = removeCoverFromCovers.Field()
    reordercoveroncovers = reorderCoverOnCovers.Field()
    setdesigntobookdesign = setDesignToBookDesign.Field()


    createbookdesign = createBookDesign.Field()
    deletebookdesign = deleteBookDesign.Field()


    approve = approve.Field()
    createcover = createCover.Field()
    deletecover = deleteCover.Field()


    createsection = createSection.Field()
    deletesection = deleteSection.Field()
    addchaptertochapters = addChapterToChapters.Field()
    removechapterfromchapters = removeChapterFromChapters.Field()
    reorderchapteronchapters = reorderChapterOnChapters.Field()


    createchapter = createChapter.Field()
    deletechapter = deleteChapter.Field()
    addcommenttocomments = addCommentToComments.Field()
    removecommentfromcomments = removeCommentFromComments.Field()
    reordercommentoncomments = reorderCommentOnComments.Field()


    resolve = resolve.Field()
    createcomment = createComment.Field()
    deletecomment = deleteComment.Field()
    setusertobooktypeuser = setUserToBookTypeUser.Field()
    addsubcommenttosubcomments = addSubCommentToSubcomments.Field()
    removesubcommentfromsubcomments = removeSubCommentFromSubcomments.Field()
    reordersubcommentonsubcomments = reorderSubCommentOnSubcomments.Field()


    createsubcomment = createSubComment.Field()
    deletesubcomment = deleteSubComment.Field()
    setusertobooktypeuser = setUserToBookTypeUser.Field()


    createbookstatus = createBookStatus.Field()
    deletebookstatus = deleteBookStatus.Field()


    createbookmetadata = createBookMetadata.Field()
    deletebookmetadata = deleteBookMetadata.Field()


    createrole = createRole.Field()
    deleterole = deleteRole.Field()


    createactivity = createActivity.Field()
    deleteactivity = deleteActivity.Field()






schema = graphene.Schema(query=Query, mutation=Mutation)
