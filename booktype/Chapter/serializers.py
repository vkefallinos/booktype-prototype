from models import Chapter
from rest_framework import serializers


class ChapterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Chapter
        fields = ('title','content','status','comments',)
