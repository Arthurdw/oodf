# Project is under an MIT-style license that can be found in the LICENSE file at the monorepo
# Monorepo: https://github.com/Arthurdw/oodf/libraries/python

from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import List, Union, Optional

tokens: List[TokenType] = []


@dataclass
class TokenType:
    represents: str  # The string representation of the token

    sot: Union[str, List[str]]  # start of token, None means any character
    eot: Union[str, List[str]]  # end of token

    regex: Optional[int] = None  # The regex flag for the token. 0 = sot, 1 = eot, 2 = both
    content: Optional[bool] = False  # True if the sot is the content of the token

    def __post_init__(self):
        tokens.append(self)


"""
All token types, defines the behaviour of the language.
"""

# Comments
TokenType("SINGLE-LINE-COMMENT", "/-/", "\n")
TokenType("MULTI-LINE-COMMENT", "/--", "--/")

# Keynotes
TokenType("SINGLE-LINE-KEYNOTE", "/!/", "\n")
TokenType("MULTI-LINE-KEYNOTE", "/!!", "!!/")

# TODO: Implement the following tokens
# # Variable
# TokenType("VARIABLE", "([a-z|A-Z])", ["\n", ";"], regex=0)
#
# # Values
# TokenType("STRING", '"', '"')
# TokenType("MULTI-LINE-STRING", '"""', '"""')
# TokenType("INTERPOLATED-STRING", "`", "`")
# TokenType("MULTI-LINE-INTERPOLATED-STRING", "```", "```")
# TokenType("NUMBER", "([0-9])", ["\n", ";", " "], content=True)
# TokenType("BOOLEAN", ["true", "false"], ["\n", ";", " "], content=True)
# TokenType("NULL", ["null"], ["\n", ";", " "], content=True)
# TokenType("COLLECTION", "[", "]")
# TokenType("OBJECT", "{", "}")
# TokenType("OBJECT-PROPERTY", "([a-z|A-Z])", ["\n", ","], regex=0)
