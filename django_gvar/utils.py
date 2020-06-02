"""
"""
import re
from json import loads

from gvar._gvarcore import GVar  # pylint: disable=E0611
from gvar import gvar  # pylint: disable=E0611


_NUMBERS = "[0-9\-\+\.\,eg]+"


def parse_gvar(expr: str, delimeter=",", cov_split="|") -> GVar:
    """
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
    if "(" in expr:
        out = gvar([gvar(val) for val in expr.split(delimeter)])
    else:
        out = gvar(*(loads(el) for el in expr.split(cov_split)))

    return out
