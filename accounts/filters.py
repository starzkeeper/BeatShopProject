import django_filters


class UserFilter(django_filters.FilterSet):
    date_joined_gte = django_filters.DateFilter(field_name='date_joined', lookup_expr='gte')
    date_joined_lte = django_filters.DateFilter(field_name='date_joined', lookup_expr='lte')
