from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_cover(img):
    if img.width != img.height:
        raise ValidationError(
            _("%(img)s is not a square"),
            params={"img": img},
        )
