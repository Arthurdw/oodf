# Project is under an MIT-style license that can be found in the LICENSE file at the monorepo
# Monorepo: https://github.com/Arthurdw/oodf/libraries/python

import unittest

from . import get_sample


class TestComments(unittest.TestCase):
    data = get_sample("comments")

    def test_comments(self):
        # TODO: implement function which asserts
        self.assertEqual(self.data, {}, "Comments should be removed")
