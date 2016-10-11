from models import BookMetadata
from rest_framework import serializers


class BookMetadataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BookMetadata
        fields = ('title','short_title','subtitle','publisher','publication_date','copyright_date','copyright_holder','publisher_city','short_description','long_description','ebook_isbn','print_isbn',)
