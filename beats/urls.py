from django.urls import path
from .views import BeatListCreateAPIView, BeatSearchAPIView

urlpatterns = [
    path("", BeatListCreateAPIView.as_view(), name='beat-list-create'),
    path('search/', BeatSearchAPIView.as_view(), name='beat-search'),
]