from django.urls import path
from .views import BeatListCreateAPIView
from rest_framework import routers
from search.views import BeatDocumentView

router = routers.DefaultRouter(trailing_slash=False)

router.register(r'beat-search', BeatDocumentView, basename='beat-search')

urlpatterns = [
    path("", BeatListCreateAPIView.as_view(), name='beat-list-create'),
]

urlpatterns += router.urls
