from django.contrib.auth import get_user_model
from rest_framework.generics import ListAPIView
from .serializers import UserSerializer
import django_filters
from .filters import UserFilter
from .pagination import UserPagination


# Create your views here.
class UserListView(ListAPIView):
    serializer_class = UserSerializer
    queryset = get_user_model().objects.all()
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_class = UserFilter
    pagination_class = UserPagination
