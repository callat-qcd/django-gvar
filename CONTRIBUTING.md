# Contributing to django-gvar

Thank you for considering contributing to `django-gvar`.
On this page, we line out of how to best help out.
And of course, please make sure you are welcoming and friendly (see also the [Python community code of conduct](https://www.python.org/psf/conduct/)).

## Guiding principles

This module is an open-source project which incorporates [G. Peter Lepage's gaussian random variables](https://github.com/gplepage/gvar) in [Django](https://www.djangoproject.com)'s ORM.
Hence, it is one of our guiding principles to stay as close as possible to both packages, which allows utilizing existing functionality, resources, and staying compatible as much as possible.

## What we are looking for

Contributions which **simplify** working with `GVars` and improve **stability and longevity** of this extended data type in ORMs.

## Community: questions & discussions

If you find a potential bug, do not hesitate to contact us and file an issue---we will try to address it as soon as possible.
But also, if you feel you have an idea for potential improvement, we welcome issues on feature requests and enhancements.

#### Filing Bugs

When filing a bug report, please let us know:

1. What is your Python, Django, and GVar version?
2. What did you do?
3. What did you expect to see?
4. What did you see instead?

## Your first contribution

We appreciate help in the form of pull requests---take a look at open issues and try identifying a problem you like to work on.
To start development, please fork this repository (`master` branch) and install the development dependencies
```bash
pip install --user -e .[dev]
```

We try to follow [PEP8](https://www.python.org/dev/peps/pep-0008/) as much as useful (see also [Flake8](https://flake8.pycqa.org/en/latest/)).
In this context, we also appreciate formatting along the lines of [black---the uncompromising Python code formatter](https://github.com/psf/black).

Before you submit pull requests, please:

1. make sure all tests work
```bash
pytest tests/
```
2. the code is linted and
```bash
flake8
```
3. the code is formatted
```bash
black --check .
```

### Versioning

`django-gvar` follows [Semantic Versioning 2.0.0](https://semver.org) (`MAJOR.MINOR.PATCH`).
Branches start with a `v`, e.g., `v1.1.0`, and once merged into master will obtain the previous branch name as a tag.
