# -*- coding: utf-8 -*-
"""Setup file for django_gvar."""

__author__ = "@ckoerber"

from os import path
from re import search, M

from setuptools import setup

CWD = path.abspath(path.dirname(__file__))

with open(path.join(CWD, "README.md"), encoding="utf-8") as inp:
    LONG_DESCRIPTION = inp.read()

with open(path.join(CWD, "requirements.txt"), encoding="utf-8") as inp:
    REQUIREMENTS = [el.strip() for el in inp.read().split(",")]

with open(path.join(CWD, "requirements-dev.txt"), encoding="utf-8") as inp:
    REQUIREMENTS_DEV = [el.strip() for el in inp.read().split(",")]

FILEDIR = path.dirname(__file__)
VERSIONFILE = path.join(FILEDIR, "django_gvar", "_version.py")


def _get_version():
    """Reads in ther version file without importing the module."""
    with open(VERSIONFILE, "rt") as inp:
        version_string = inp.read()
    match = search(r"^__version__\s*=\s*['\"]{1}([^'\"]*)['\"]{1}", version_string, M)
    if match:
        return match.group(1)
    else:
        raise RuntimeError("Unable to find version string in %s." % (VERSIONFILE,))


setup(
    name="django_gvar",
    version=_get_version(),
    description=None,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url=None,
    author=__author__,
    author_email="software@ckoerber.com",
    keywords=[],
    packages=["django_gvar"],
    install_requires=REQUIREMENTS,
    extras_require={"dev": REQUIREMENTS_DEV},
)
