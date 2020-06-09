"""Forms for testing."""

from django.forms import ModelForm, Textarea
from field_tests.models import ExampleTable


class ExampleForm(ModelForm):
    """Form for example table's GVarField."""

    class Meta:
        """Specification of form model and widget."""

        model = ExampleTable
        fields = ["a"]
        widgets = {
            "a": Textarea(
                attrs={
                    "placeholder": "'1(2), 3(4), ...' or '[1, 2] | [[3, 4], [4, 5]]'",
                    "class": "form-control",
                },
            )
        }
