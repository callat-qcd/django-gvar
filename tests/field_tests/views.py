"""Views of test project."""
from django.views import View
from django.views.generic.edit import FormView

from django.http import HttpResponseNotFound, HttpResponseRedirect

from field_tests.models import ExampleTable
from field_tests.forms import ExampleForm


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
        """Save model instance if form is valid."""
        form.save()
        return super().form_valid(form)


class DeleteAllView(View):
    """POST only view for deleting all ExampleTable model entries."""

    def get(self, request):
        """Not accessible over GET request."""
        return HttpResponseNotFound()

    def post(self, request):
        """Delete all present ExampleTable entries."""
        ExampleTable.objects.all().delete()
        return HttpResponseRedirect("/")
