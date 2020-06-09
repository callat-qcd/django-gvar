"""Checks if the views are available."""
from django.test import TestCase

from gvar import gvar

from field_tests.models import ExampleTable


class ViewsTestCase(TestCase):
    """Tests if example views are present."""

    def test_01_index_present(self):
        """Logs into index page."""
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_02_post_gvar(self):
        """Checks if posting to index inserts gvars."""
        response = self.client.get("/")
        form = response.context["form"]
        data = form.initial
        data["a"] = "1 | 2"
        response = self.client.post("/", data=data, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(ExampleTable.objects.count(), 1)
        self.assertEqual(ExampleTable.objects.first().a, gvar(1, 2))
