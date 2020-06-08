
# Details

This module implements a [custom model field](https://docs.djangoproject.com/en/dev/howto/custom-model-fields/) for GVars.
The GVars are stored in JSON format and inherit in [Django's `JSONFields`](https://docs.djangoproject.com/en/dev/ref/models/fields/#django.db.models.JSONField).

This module utilizes `gvar`s `gloads` and `gdumps` to replace the custom encode and decoder to read and write from and to the database.
Thus, all GVar supported types are supported.

A custom `GVarFormField` simplifies the user interface on web forms.
This field uses custom string parsers to convert text input to GVars.
For now, this only includes arrays of GVars or single GVars.

* GVars without correlations are can specified by lists of numbers where parenthesis define standard deviations
```text
1(2), 3(4), ...
```
* GVars with correlations are specified as arrays of mean values and the covariance matrix separated by a `|`
```text
[1, 2] | [[1, 2], [2, 3]]
```

Migration files store the `gvar` version number (which specify details about tables), to ensure reproducibility in the extraction of stored data.
