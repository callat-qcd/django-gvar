"""Utility functions.

Provides:
    * parse_gvar to convert string to gvars
"""
from json import loads

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from gvar._gvarcore import GVar
from gvar import gvar


def parse_gvar(expr: str, delimeter=",", cov_split="|") -> GVar:
    """Converts string to gvars.

    Options:
        single gvar:
            * 1(2)
            * 1 | 2
        multiple uncorrelated:
            * 1(2), 3(4), 5(6), ...
            * [1, 3, 5, ...] | [2, 4, 6, ...]
        multiple correlated:
            * [1, 3, 5...] | [[2, 4, 6, ...], []]
    """
    expr = expr.strip()
    try:
        if "(" in expr:
            arr = [gvar(val) for val in expr.split(delimeter)]
            out = arr[0] if len(arr) == 1 else gvar(arr)
        else:
            out = gvar(*(loads(el) for el in expr.split(cov_split)))
    except Exception as e:
        raise ValidationError(
            _("Failed to parse GVars. Here are the details:\n") + str(e)
        )

    return out
