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
    python_requires=">=3.6",
    version=_get_version(),
    description="Django extension which adds model fields to store"
    " multi-dimensional Gaussian random variables.",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url="https://github.com/callat-qcd/django-gvar",
    project_urls={
        "Bug Reports": "https://github.com/callat-qcd/django-gvar/issues",
        "Source": "https://github.com/callat-qcd/django-gvar",
        "Documentation": "https://django-gvar.readthedocs.io",
    },
    author=__author__,
    author_email="software@ckoerber.com",
    keywords=["Database", "Django", "GVar", "Statistics"],
    packages=["django_gvar"],
    install_requires=REQUIREMENTS,
    extras_require={"dev": REQUIREMENTS_DEV},
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "Topic :: Database :: Database Engines/Servers",
        "Topic :: Database",
        "Topic :: Scientific/Engineering",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Framework :: Django :: 3.1",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: BSD License",
    ],
)
