"""Utility functions for checking gvar fields."""

from numpy.testing import assert_allclose as assert_array_allclose

from gvar._gvarcore import GVar
from gvar import mean, sdev, evalcov


def assert_allclose(
    actual: GVar,
    desired: GVar,
    rtol: float = 1e-07,
    atol: float = 0,
    equal_nan: bool = True,
    err_msg: str = "",
    verbose: bool = True,
    test_cov: bool = True,
):
    """Runs numpys all close on mean, sdev and covariance of gvars.

    Arguments:
        actual, desired: To be tested GVars, can be numbers, arrays or dicts
        see numpy.testing.assert_allclose
        test_cov: If true, also checks if covariance is equal up to request precision.
    """
    if hasattr(actual, "keys") and hasattr(actual, "keys"):
        if set(actual.keys()) == set(desired.keys()):
            for key, val in actual.items():
                assert_allclose(
                    val,
                    desired[key],
                    rtol=rtol,
                    atol=atol,
                    equal_nan=equal_nan,
                    err_msg=err_msg,
                    verbose=verbose,
                )
            return
        else:
            raise ValueError("actual and desired have mismatched keys")
    else:

        tests = [mean, sdev] + ([evalcov] if test_cov else [])
        for attr in tests:
            assert_array_allclose(
                attr(actual),
                attr(desired),
                rtol=rtol,
                atol=atol,
                equal_nan=equal_nan,
                err_msg=f"Error in {attr.__name__}" + err_msg,
                verbose=verbose,
            )
