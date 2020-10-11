from django_filters.rest_framework import FilterSet, filters
from api.models import *


class UserFilter(FilterSet):
    email = filters.CharFilter(method='user_email_filter')
    name = filters.CharFilter(method='user_name_filter')

    def user_email_filter(self, queryset, email, value):
        email = self.request.query_params.get(email, value)
        if email is not None:
            queryset = queryset.filter(email__icontains=value)
        return queryset

    def user_name_filter(self, queryset, name, value):
        name = self.request.query_params.get(name, value)
        if name is not None:
            queryset = queryset.filter(name__icontains=value)
        return queryset
