# Project is under an MIT-style license that can be found in the LICENSE file at the monorepo
# Monorepo: https://github.com/Arthurdw/oodf/libraries/python

from __future__ import annotations

from typing import TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .lexer import Token
    from typing import Dict, Any, List

key_type = Union[str, int, float, bool, None]


def transpile(tokens: List[Token]) -> Dict[key_type, Union[key_type, Dict[key_type, Any]]]:
    """
    Transpile a collection of tokens into a python dictionary.

    Parameters:
    -----------
    tokens: List[:class:`oodf.core.lexer.Token`]
        The collection of tokens whom must be transpiled.
        This collection can be retrieved through the lexer output. (tokenize)
    """
    # TODO: Implement transpiler
    return {"transpiler": "todo"}
