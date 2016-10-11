from models import BookDesign
from rest_framework import serializers


class BookDesignSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BookDesign
        fields = ('theme','heading','color','font_size','alignment','paragraph','text_indent','line_height',)
