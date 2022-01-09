# Project is under an MIT-style license that can be found in the LICENSE file at the monorepo
# Monorepo: https://github.com/Arthurdw/oodf/libraries/python
from typing import Dict


class Lexer:
    def __init__(self, content: str):
        self.content = content

    def tokenize(self) -> Dict[str, str]:
        # TODO: Properly tokenize
        return {"lexer": "todo"}
