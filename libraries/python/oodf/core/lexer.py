# Project is under an MIT-style license that can be found in the LICENSE file at the monorepo
# Monorepo: https://github.com/Arthurdw/oodf/libraries/python

from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Tuple

from ..tokens import tokens

if TYPE_CHECKING:
    from .transpiler import key_type
    from ..tokens import TokenType
    from typing import List, Union, Dict, Any


@dataclass
class Token:
    type: TokenType
    content: Union[key_type, List[key_type], Dict[key_type, Union[key_type, Any]]]


CachedToken = Tuple[int, bool, Token]


def tokenize(content: str) -> List[Token]:
    """
    Tokenize OODF syntax.

    Parameters:
    -----------
    content: :class:`str`
        A string in OODF syntax.
    """
    registered_tokens: List[Token] = []

    __tkn_cache: Dict[TokenType, CachedToken] = {}

    print(tokens)

    return registered_tokens
