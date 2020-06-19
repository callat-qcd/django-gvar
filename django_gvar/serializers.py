"""Encoder supporting mixed entries of GVars, numpy arrays and regular Python objects."""
from re import compile, DOTALL, MULTILINE
from json import JSONDecoder, loads, dumps
from json.scanner import make_scanner as json_make_scanner

from numpy import ndarray, array

from django.core.serializers.json import DjangoJSONEncoder

from gvar._gvarcore import GVar
from gvar import gdumps, gloads


class GVarJSONEncoder(DjangoJSONEncoder):
    """Encode adding numpy and GVar support to the Dajngo JSON encoder."""

    def default(self, o):
        """Extends the dtypes known by Djangos JSONEncoder to numpy arrays and GVars.

        Numpy arrays are converted to list and then passed to the original JSONEncoder
        and GVars are dumped using gvar.gdumps.
        """
        if isinstance(o, GVar) or (
            isinstance(o, ndarray) and isinstance(o.flat[0], GVar)
        ):
            return f"gvar({gdumps(o)})"
        elif isinstance(o, ndarray) and o.dtype is not object:
            return f"array({dumps(o.tolist())})"
        else:
            return super().default(o)


PATTERN = compile(r"^(gvar|array)\((.*)\)$", DOTALL | MULTILINE)


def decode_objects(obj):
    """
    """
    if isinstance(obj, str):
        obj = decode_string(obj)
    elif isinstance(obj, dict):
        for key, val in obj.items():
            obj[key] = decode_objects(val)

    return obj


def decode_string(string):
    match = PATTERN.search(string)
    if match:
        if match.group(1) == "gvar":
            obj = gloads(match.group(2))
            if isinstance(obj, ndarray) and obj.size == 1:
                obj = obj.flat[0]
        elif match.group(1) == "array":
            obj = array(loads(match.group(2)))
        else:
            raise ValueError
    else:
        obj = string

    return obj


class GVarJSONDecoder(JSONDecoder):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.json_scan_once = json_make_scanner(self)
        self.scan_once = self._scan_once

    def _scan_once(self, string, idx):
        obj, next_idx = self.json_scan_once(string, idx)
        obj = decode_objects(obj)
        return obj, next_idx
