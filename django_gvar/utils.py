"""Utility functions.

Provides:
    * parse_gvar to convert string to gvars
"""
from json import loads

from numpy import ndarray, array2string

from gvar._gvarcore import GVar
from gvar import gvar, mean, evalcov


def parse_str_to_gvar(expr: str, delimeter=",", cov_split="|") -> GVar:
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

    Todo:
        Support buffer dicts
    """
    expr = expr.strip()
    if "(" in expr:
        arr = [gvar(val) for val in expr.split(delimeter)]
        out = arr[0] if len(arr) == 1 else gvar(arr)
    else:
        out = gvar(*(loads(el) for el in expr.split(cov_split)))

    return out


def parse_gvar_to_str(obj: GVar) -> str:
    """Inverts `parse_str_to_gvar`."""
    if obj is None:
        return ""
    elif isinstance(obj, str):
        return obj
    elif isinstance(obj, ndarray):
        return (
            array2string(mean(obj), separator=",", formatter={"float": str})
            + " | "
            + array2string(evalcov(obj), separator=",", formatter={"float": str})
        )
    elif isinstance(obj, GVar):
        return str(mean(obj)) + " | " + str(evalcov(obj))
    else:
        raise TypeError(f"Cannot parse {obj} ({type(obj)}) to str")
