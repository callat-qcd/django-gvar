from django.test import TestCase

# Create your tests here.
from gvar import gvar
from numpy.testing import assert_array_equal

from field_tests.models import TestTable


class GvarFieldTestCase(TestCase):
    """Tests for the gvar field
    """

    def test_gvar_dump_load(self):
        """Dumps gvar to db, reads it off and checks if gvars are equal
        """
        a = gvar([1, 2, 3], [[4, 5, 6], [5, 8, 7], [6, 7, 9]])

        TestTable(a=a).save()

        a_stored = TestTable.objects.first().a

        assert_array_equal(a, a_stored)
