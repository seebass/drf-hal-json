from collections import OrderedDict

from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.settings import api_settings

from drf_hal_json import LINKS_FIELD_NAME, EMBEDDED_FIELD_NAME


class HalPageNumberPagination(PageNumberPagination):
    page_size_query_param = "page_size"
    max_page_size = 1000000

    def get_paginated_response(self, data):
        result = OrderedDict()
        links = OrderedDict()
        links[api_settings.URL_FIELD_NAME] = self.request.build_absolute_uri()
        links['next'] = self.get_next_link()
        links['previous'] = self.get_previous_link()
        result[LINKS_FIELD_NAME] = links
        result['count'] = self.page.paginator.count
        result['page_size'] = self.get_page_size(self.request)
        result[EMBEDDED_FIELD_NAME] = data
        return Response(result)
