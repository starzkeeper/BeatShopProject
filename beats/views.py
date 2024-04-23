from rest_framework.generics import ListCreateAPIView

from .models import Beat
from .serializers import BeatSerializer
from .mixins import ActiveQuerySetMixin
from .filters import BeatFilter
import django_filters
from .pagination import BeatPagination


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
