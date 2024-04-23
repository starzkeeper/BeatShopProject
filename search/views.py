from django_elasticsearch_dsl_drf.constants import LOOKUP_FILTER_RANGE, LOOKUP_FILTER_TERMS, LOOKUP_FILTER_TERM
from django_elasticsearch_dsl_drf.filter_backends import CompoundSearchFilterBackend, FilteringFilterBackend
from django_elasticsearch_dsl_drf.viewsets import DocumentViewSet
from elasticsearch_dsl import Q

from .documents import BeatDocument
from .serializers import BeatDocumentSerializer


class BeatDocumentView(DocumentViewSet):
    document = BeatDocument
    serializer_class = BeatDocumentSerializer

    filter_backends = [
        CompoundSearchFilterBackend,
        FilteringFilterBackend
    ]

    search_fields = {
        'name': {'fuzziness': 'AUTO'},
    }
    filter_fields = {
        'author': 'username.raw',
        'bpm': 'bpm.raw',
        'key': 'key.raw',
        'genre': 'genre.raw',
        'tags': 'tags.raw',
        'active': 'active.raw',
        'uploaded': 'uploaded.raw',
        'price': 'price.raw'
    }


