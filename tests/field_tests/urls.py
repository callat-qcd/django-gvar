"""URLs for tests to check rendering of gvars."""
from django.urls import path

from field_tests.views import IndexView

urlpatterns = [
    path("", IndexView.as_view()),
]
