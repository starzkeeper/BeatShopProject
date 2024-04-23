from django.contrib.auth import get_user_model
from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry
from beats.models import Beat


@registry.register_document
class UserDocument(Document):
    id = fields.IntegerField(
        attr='id'
    )
    username = fields.TextField(
        attr='username',
        fields={
            'raw': fields.KeywordField()
        }
    )

    class Index:
        name = 'users'
        settings = {
            'number_of_shards': 1,
            'number_of_replicas': 0,
        }

    class Django:
        model = get_user_model()


@registry.register_document
class BeatDocument(Document):
    name = fields.TextField(
        attr='name',
        fields={
            'raw': fields.TextField()
        }
    )
    author = fields.ObjectField(
        attr='author',
        properties={
            'id': fields.IntegerField(),
            'username': fields.TextField(
                attr='username',
                fields={
                    'raw': fields.KeywordField()
                }
            ),
        }
    )
    description = fields.KeywordField(
        attr='description',
        fields={
            'raw': fields.KeywordField()
        }
    )
    bpm = fields.IntegerField(
        attr='bpm',
        fields={
            'raw': fields.IntegerField()
        }
    )
    key = fields.KeywordField(
        attr='key',
        fields={
            'raw': fields.KeywordField()
        }
    )
    tags = fields.TextField(
        attr='tags_indexing',
        fields={
            'raw': fields.KeywordField(multi=True)
        },
        multi=True
    )
    slug = fields.KeywordField(
        attr='slug'
    )
    active = fields.BooleanField(
        attr='active',
        fields={
            'raw': fields.BooleanField()
        }
    )
    genre = fields.KeywordField(
        attr='genre',
        fields={
            'raw': fields.KeywordField()
        }
    )
    uploaded = fields.DateField(
        attr='uploaded',
        fields={
            'raw': fields.DateField()
        }
    )
    price = fields.IntegerField(
        attr='price',
        fields={
            'raw': fields.IntegerField()
        }
    )

    class Index:
        name = 'beats'
        settings = {
            'number_of_shards': 1,
            'number_of_replicas': 0,
        }

    class Django:
        model = Beat
