# Project is under an MIT-style license that can be found in the LICENSE file at the monorepo
# Monorepo: https://github.com/Arthurdw/oodf/libraries/python

from unittest import TestCase

from libraries.python.oodf import load
from libraries.python.oodf.core import tokenize
from libraries.python.oodf.core.lexer import Token
from libraries.python.oodf.exceptions import InvalidSyntax, ExpectedEOT
from libraries.python.tests import token_types
from libraries.python.tests.utils import get_sample


class TestComments(TestCase):
    data = get_sample("variables")
    tokens = [
        Token(token_types["VARIABLE"], "welcome = \"Hello World!\""),
        Token(token_types["VARIABLE"], "foo \"bar\""),
        Token(token_types["VARIABLE"], "bar \"foo\""),
        Token(token_types["VARIABLE"], "number 1"),
        Token(token_types["VARIABLE"], "float 3.14"),
        Token(token_types["VARIABLE"], "yes true"),
        Token(token_types["VARIABLE"], "no false"),
        Token(token_types["VARIABLE"], "collecction [1, 2, 3]"),
        Token(token_types["VARIABLE"], "nullValue null"),
    ]
    parsed = {
        "welcome": "Hello World!",
        "foo": "bar",
        "bar": "foo",
        "number": 1,
        "float": 3.14,
        "yes": True,
        "no": False,
        "collecction": [1, 2, 3],
        "nullValue": None,
    }

    def test_variable_tokenize(self):
        self.assertEqual(self.tokens, tokenize(self.data), "Should tokenize variables")

    def test_variable_parse(self):
        self.assertEqual(self.parsed, load(self.data), "Should parse variables")

    def test_variable_raises_invalid_syntax(self):
        self.assertRaises(InvalidSyntax, tokenize, "a =")
        self.assertRaises(InvalidSyntax, tokenize, "= 'b'")

    def test_variable_raises_expected_eot(self):
        self.assertRaises(ExpectedEOT, tokenize, "a = 'b'")
        self.assertRaises(ExpectedEOT, tokenize, "a 'b'")
