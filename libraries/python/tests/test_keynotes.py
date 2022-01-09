# Project is under an MIT-style license that can be found in the LICENSE file at the monorepo
# Monorepo: https://github.com/Arthurdw/oodf/libraries/python

from unittest import TestCase
from libraries.python.tests.utils import get_sample


class TestKeynotes(TestCase):
    data = get_sample("keynotes")

    def test_keynotes(self):
        # TODO: implement function which asserts
        self.assertEqual(self.data, {}, "Keynotes should be removed for transpilation")
