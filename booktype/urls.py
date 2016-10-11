from django.contrib import admin
from graphene_django.views import GraphQLView
from django.conf.urls import url, include
from rest_framework import routers, response, schemas, renderers
from rest_framework.decorators import api_view, renderer_classes
from rest_framework_swagger.renderers import OpenAPIRenderer, SwaggerUIRenderer



@api_view()
@renderer_classes([SwaggerUIRenderer, OpenAPIRenderer, renderers.CoreJSONRenderer])
def schema_view(request):
    generator = schemas.SchemaGenerator(title='booktype API')
    return response.Response(generator.get_schema(request=request))





from booktype.BookTypeUser.views import BookTypeUserViewSet
from booktype.BookTypeGroup.views import BookTypeGroupViewSet
from booktype.Book.views import BookViewSet
from booktype.BookDesign.views import BookDesignViewSet
from booktype.Cover.views import CoverViewSet
from booktype.Section.views import SectionViewSet
from booktype.Chapter.views import ChapterViewSet
from booktype.Comment.views import CommentViewSet
from booktype.SubComment.views import SubCommentViewSet
from booktype.BookStatus.views import BookStatusViewSet
from booktype.BookMetadata.views import BookMetadataViewSet
from booktype.Role.views import RoleViewSet
from booktype.Activity.views import ActivityViewSet

router = routers.DefaultRouter()
router.register(r'booktypeusers', BookTypeUserViewSet)
router.register(r'booktypegroups', BookTypeGroupViewSet)
router.register(r'books', BookViewSet)
router.register(r'bookdesigns', BookDesignViewSet)
router.register(r'covers', CoverViewSet)
router.register(r'sections', SectionViewSet)
router.register(r'chapters', ChapterViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'subcomments', SubCommentViewSet)
router.register(r'bookstatuses', BookStatusViewSet)
router.register(r'bookmetadatas', BookMetadataViewSet)
router.register(r'roles', RoleViewSet)
router.register(r'activities', ActivityViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^api/', include(router.urls)),
    url(r'^admin/', admin.site.urls),
    url(r'^graphql', GraphQLView.as_view(graphiql=True)),
    url(r'^swagger', schema_view),
]
