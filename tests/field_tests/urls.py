"""URLs for tests to check rendering of gvars."""
from django.urls import path

from field_tests.views import IndexView, DeleteAllView

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("delete/", DeleteAllView.as_view(), name="delete"),
]
