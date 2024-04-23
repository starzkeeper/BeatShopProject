from rest_framework import serializers
from django_elasticsearch_dsl_drf.serializers import DocumentSerializer
from .documents import BeatDocument, UserDocument


class SearchQuerySerializer(serializers.Serializer):
    query = serializers.CharField(max_length=200)


class UserDocumentSerializer(DocumentSerializer):
    class Meta:
        document = UserDocument

        fields = (
            'id',
            'username'
        )


class BeatDocumentSerializer(DocumentSerializer):
    class Meta:
        document = BeatDocument

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
