"""Views of test project."""
from django.views.generic.edit import FormView
from django.forms import ModelForm, Textarea

from field_tests.models import ExampleTable


class ExampleForm(ModelForm):
    class Meta:
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


class IndexView(FormView):
    """View to test GVar form and rendering."""

    template_name = "index.html"
    form_class = ExampleForm
    success_url = "/"

    def get_context_data(self, **kwargs):
        """Adds form and existing GVar entries to index template."""
        context = super().get_context_data(**kwargs)
        context["entries"] = ExampleTable.objects.all()
        return context

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
