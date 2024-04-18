from django.contrib.auth import get_user_model
from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry
from beats.models import Beat


@registry.register_document
class UserDocument(Document):
    class Index:
        name = 'users'
        settings = {
            'number_of_shards': 1,
            'number_of_replicas': 0,
        }

    class Django:
        model = get_user_model()
        fields = [
            'id',
            'username',
            'first_name',
            'last_name',
            'date_joined',
            'email'

        ]


@registry.register_document
class BeatDocument(Document):
    # name = fields.TextField()
    author = fields.ObjectField(properties={
        'id': fields.IntegerField(),
        'first_name': fields.TextField(),
        'last_name': fields.TextField(),
        'username': fields.TextField(),
    })
    # description = fields.TextField(index=False)

    class Index:
        name = 'beats'
        settings = {
            'number_of_shards': 1,
            'number_of_replicas': 0,
        }

    class Django:
        model = Beat
        fields = [
            'id',
            'name',
            'description',
            'bpm', 'key', 'tags',
            'slug', 'active', 'genre',
            'uploaded',
            'price'
        ]
