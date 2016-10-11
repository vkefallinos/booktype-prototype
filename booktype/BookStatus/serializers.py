from models import BookStatus
from rest_framework import serializers


class BookStatusSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BookStatus
        fields = ('status',)
