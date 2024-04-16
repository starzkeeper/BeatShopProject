import django_filters


class BeatFilter(django_filters.FilterSet):
    price_gte = django_filters.NumberFilter(field_name='price', lookup_expr='gte')
    price_lte = django_filters.NumberFilter(field_name='price', lookup_expr='lte')
    bpm_gte = django_filters.NumberFilter(field_name='bpm', lookup_expr='gte')
    bpm_lte = django_filters.NumberFilter(field_name='bpm', lookup_expr='lte')


