from rest_framework import serializers
from .models import Beat
from accounts.serializers import UserSerializer
from taggit.serializers import TaggitSerializer, TagListSerializerField


class BeatSerializer(TaggitSerializer, serializers.ModelSerializer):
    author = UserSerializer()
    tags = TagListSerializerField()

    class Meta:
        model = Beat
        fields = (
            'id',
            'name',
            'author',
            'description',
            'bpm', 'key', 'tags',
            'slug', 'active', 'genre',
            'uploaded',
            'price'
        )
