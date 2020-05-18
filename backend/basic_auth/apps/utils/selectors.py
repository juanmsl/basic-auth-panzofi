from typing import Any

from django.core.exceptions import ObjectDoesNotExist
from django.utils.translation import ugettext_lazy as _
from rest_framework import exceptions


def get_or_404(
    model: Any,
    **args
) -> Any:

    try:
        model_object = model.objects.get(
            **args
        )
    except ObjectDoesNotExist:
        msg = _('Not found.')
        raise exceptions.ValidationError(msg)

    return model_object
