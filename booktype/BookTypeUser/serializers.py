from models import BookTypeUser
from rest_framework import serializers


class BookTypeUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BookTypeUser
        fields = ('email','fullName','about','profile_image','public_email','twitter','facebook','linked_in','youtube','vimeo','hashed_password','preferred_Language',)
