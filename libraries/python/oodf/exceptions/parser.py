# Project is under an MIT-style license that can be found in the LICENSE file at the monorepo
# Monorepo: https://github.com/Arthurdw/oodf/libraries/python
from .base import OODFException


class ParserException(OODFException):
    """Represents an exception which occurs during the parsing of OODF syntax."""


class InvalidSyntax(ParserException):
    """Exception thrown when syntax does not match the expected syntax/is invalid OODF."""


class ExpectedEOT(InvalidSyntax):
    """Exception thrown when the EOF is reached but no EOT was found."""
