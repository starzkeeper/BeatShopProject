from elasticsearch_dsl import Q
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView

from .models import Beat
from .serializers import BeatSerializer
from .mixins import ActiveQuerySetMixin
from .filters import BeatFilter
import django_filters
from .pagination import BeatPagination
from search.views import ElasticSearchAPIView
from search.documents import BeatDocument


# Create your views here.
class BeatListCreateAPIView(ActiveQuerySetMixin, ListCreateAPIView):
    serializer_class = BeatSerializer
    allow_staff_view = True
    allow_superuser_field = True
    queryset = Beat.objects.all()
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_class = BeatFilter
    pagination_class = BeatPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class BeatSearchAPIView(ElasticSearchAPIView):
    serializer_class = BeatSerializer
    document_class = BeatDocument

    def generate_q_expression(self, query):
        return Q(
                'multi_match', query=query,
                fields=[
                    'name', 'author.username'
                ], fuzziness='auto')
