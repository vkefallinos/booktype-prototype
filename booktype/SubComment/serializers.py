from models import SubComment
from rest_framework import serializers


class SubCommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SubComment
        fields = ('text','user',)
