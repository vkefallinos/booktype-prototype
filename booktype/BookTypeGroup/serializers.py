from models import BookTypeGroup
from rest_framework import serializers


class BookTypeGroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BookTypeGroup
        fields = ('name','description','image','owner','members','books',)
