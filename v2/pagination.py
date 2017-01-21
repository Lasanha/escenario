from collections import OrderedDict

from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class NumberedPagePagination(PageNumberPagination):
    def get_paginated_response(self, data):
        previous_page = self.page.previous_page_number() if \
            self.page.has_previous() else None
        next_page = self.page.next_page_number() \
            if self.page.has_next() else None


        data = OrderedDict([
             ('pageSize', self.page_size),
             ('previous', previous_page),
             ('current', self.page.number),
             ('next', next_page),
             ('totalCount', self.page.paginator.count),
             ('totalPages', self.page.paginator.num_pages),
             ('results', data)
         ])
        return Response(data)
