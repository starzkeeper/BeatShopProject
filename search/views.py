import abc
from typing import Any, Dict

from django.http import HttpResponse
from elasticsearch_dsl.query import Bool
from elasticsearch_dsl.response import Response
from elasticsearch_dsl.search import Search
from rest_framework import status
from rest_framework.response import Response as DRFResponse
from rest_framework.pagination import LimitOffsetPagination

from rest_framework.views import APIView
from .serializers import SearchQuerySerializer


class ElasticSearchAPIView(APIView, LimitOffsetPagination):
    serializer_class = None
    document_class = None

    @abc.abstractmethod
    def generate_q_expression(self, query):
        """This method should be overridden
        and return a Q() expression."""

    def get(self, request, query):
        try:
            q = self.generate_q_expression(query)
            search = self.document_class.search().query(q)
            response = search.execute()

            print(f'Found {response.hits.total.value} hit(s) for query: "{query}"')
            results = self.paginate_queryset(response, request, view=self)
            serializer = self.serializer_class(results, many=True)
            return self.get_paginated_response(serializer.data)
        except Exception as e:
            return HttpResponse(e, status=500)
