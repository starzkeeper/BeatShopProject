from django.db.models import QuerySet


class ActiveQuerySetMixin:
    user_field = 'user'
    allow_staff_view = True
    allow_superuser_field = True

    def get_queryset(self):
        user = self.request.user  # type:ignore
        qs = super().get_queryset()  # type:ignore
        if self.allow_superuser_field is True and user.is_superuser:
            return qs
        elif self.allow_staff_view is True and user.is_staff:
            return qs
        return qs.filter(active=True)
