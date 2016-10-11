from models import Cover
from rest_framework import serializers


class CoverSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cover
        fields = ('title','creator','licence','notes','image','approved',)
