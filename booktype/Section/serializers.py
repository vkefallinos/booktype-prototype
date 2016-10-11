from models import Section
from rest_framework import serializers


class SectionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Section
        fields = ('title','chapters',)
