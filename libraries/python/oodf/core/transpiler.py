# Project is under an MIT-style license that can be found in the LICENSE file at the monorepo
# Monorepo: https://github.com/Arthurdw/oodf/libraries/python

from __future__ import annotations

from typing import Dict, Union, Any

from .lexer import Lexer

key_type = Union[str, int, float, bool, None]


class Transpiler:
    def __init__(self, lexer: Lexer):
        self.lexer = lexer

    def transpile(self) -> Dict[key_type, Union[key_type, Dict[key_type, Any]]]:
        # TODO: Implement transpiler
        return {"transpiler": "todo"}
