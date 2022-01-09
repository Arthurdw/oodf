# Project is under an MIT-style license that can be found in the LICENSE file at the monorepo
# Monorepo: https://github.com/Arthurdw/oodf/libraries/python
from dataclasses import dataclass

tokens = []


@dataclass
class TokenType:
    represents: str  # The string representation of the token

    sot: str  # start of token
    eot: str  # end of token

    def __post_init__(self):
        tokens.append(self)


if len(tokens) == 0:  # First time we are initializing the tokens
    # Comments
    TokenType("SINGLE-LINE-COMMENT", "/-/", "\n")
    TokenType("MULTI-LINE-COMMENT", "/--", "--/")

    # Keynotes
    TokenType("SINGLE-LINE-KEYNOTE", "/!/", "\n")
    TokenType("MULTI-LINE-KEYNOTE", "/!!", "!!/")
