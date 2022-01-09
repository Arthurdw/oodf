# Project is under an MIT-style license that can be found in the LICENSE file at the monorepo
# Monorepo: https://github.com/Arthurdw/oodf/libraries/python

from unittest import TestCase

from libraries.python.oodf import load
from libraries.python.tests.utils import get_sample


class TestComments(TestCase):
    data = get_sample("comments")

    def test_comments_parse(self):
        # TODO: implement function which asserts
        self.assertEqual({}, load(self.data), "Comments should be removed")
