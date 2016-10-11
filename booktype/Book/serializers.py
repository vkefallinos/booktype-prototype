from models import Book
from rest_framework import serializers


class BookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Book
        fields = ('name','description','licence','language','right_to_left','public','image','status','created','published','owner','metadata','roles','chapters','sections','covers','design',)
