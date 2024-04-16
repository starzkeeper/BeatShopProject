from rest_framework import serializers
from .models import Beat
from accounts.serializers import UserSerializer


class BeatSerializer(serializers.ModelSerializer):
    author = UserSerializer()

    class Meta:
        model = Beat
        fields = (
            'id',
            'name',
            'author',
            'description',
            'bpm', 'key', 'tags',
            'slug', 'active',
            'uploaded',
            'price'
        )
