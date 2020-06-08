[![Code Coverage](https://codecov.io/gh/callat-qcd/django-gvar/branch/master/graph/badge.svg)](https://codecov.io/gh/callat-qcd/django-gvar)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)


# django-gvar

## Description

`django-gvar` allows to store [multi-dimensional Gaussian random variables implemented by G. Peter Lepage's `gvar` module](https://github.com/gplepage/gvar) into [Django](https://www.djangoproject.com)'s ORM Framework.
It adds a `GVarField` which can be used to store individual GVars, arrays of GVars and Dictionaries of GVars.

### Usage in scripts

Import the `GVarField` field into your project and use it out-of-the-box as for example a `FloatField`.

```python
# myproject.models.py
from django.db import models
from django_gvar import GVarField

class ExampleTable(models.Model):
    a = GVarField()
```

```python
from gvar import gvar
from myproject.models import ExampleTable

a = gvar([1, 2, 3], [4, 5, 6])
entry = ExampleTable(a=a)
entry.save()
```

### Usage in forms

For web-froms, the default widget for `GVarField`s are text areas.
Currently, the form supports single numbers and arrays as input.
These forms utilize custom syntax to convert the input to `GVars`:

* GVars without correlations are can specified by lists of numbers where parenthesis specify standard deviations
```text
1(2), 3(4), ...
```
* GVars with correlations are specified as arrays of mean values and the covariance matrix seperated by a `|`
```text
[1, 2] | [[1, 2], [2, 3]]
```


## Install

`django-gvar` can be installed from the repository root using `pip`
```bash
pip install [-e] [--user] .
```

Because it utilizes Django's `JSONField`, which is available for all database backends in Django version 3.1 (previously it was a Postgres only field), it currently depends on the development version of Django (`Django==3.1a1`).
Once established, the dependencies will be updated accordingly.


## Details

The underlaying database type for `django-gvar` are `JSONField`s.
It uses `gvars` `gdumps` and `gloads` to generate corresponding `JSON`.
More details can be found in the [docs]().

## Examples

The `tests` directory implement a simple Django app using the `GVarField`s.
To start it, install the repo as specified above and run
```bash
cd tests
python manage.py migrate # init that test database / only needs to be run once
python manage.py runserver # start a local server
```
