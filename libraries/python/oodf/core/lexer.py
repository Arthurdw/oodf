# Project is under an MIT-style license that can be found in the LICENSE file at the monorepo
# Monorepo: https://github.com/Arthurdw/oodf/libraries/python

from __future__ import annotations

from copy import deepcopy
from dataclasses import dataclass
from typing import TYPE_CHECKING, Tuple

from ..exceptions import ExpectedEOT, InvalidSyntax
from ..tokens import tokens

if TYPE_CHECKING:
    from .transpiler import ValidType
    from ..tokens import TokenType
    from typing import List, Union, Dict, Any


@dataclass
class Token:
    type: TokenType
    content: Union[ValidType, List[ValidType], Dict[ValidType, Union[ValidType, Any]]]


CachedToken = Tuple[int, bool, Token]


def __handle_token_cache(loc: Tuple[int, int], cache: Dict[str, CachedToken], char: str) -> bool:
    if cache:
        return False

    for tk in tokens:
        if tk.sot[0] == char:
            cache[tk.represents] = (0, False, Token(tk, ""))

    if not cache and char not in ["\n", " "]:
        raise InvalidSyntax(loc, f"Unexpected character {repr(char)}")

    return True


def __handle_character(
        loc: Tuple[int, int],
        cache: Dict[str, CachedToken],
        char: str,
        sot: str,
        token_type: str
) -> bool:
    if char == sot:
        return False

    del cache[token_type]

    if not cache:
        raise InvalidSyntax(loc, f"Unexpected character {repr(char)}, expected {repr(sot)}")

    return True


def __handle_end_character(
        cache: Dict[str, CachedToken],
        buff: List[str],
        res: List[Token],
        char: str,
        current: int,
        tk: Token
) -> Tuple[bool, int]:
    if current + 1 > len(tk.type.eot):
        current = 0

    if tk.type.eot[current] == char:
        buff.append(char)
        current += 1

        if current >= len(tk.type.eot):
            tk.content = tk.content.strip()
            res.append(tk)
            buff.clear()
            cache.clear()

            return True, current
    else:
        current = 0

        if buff:
            tk.content += "".join(buff)
            buff.clear()

        tk.content += char

    return False, current


def __lex_content(
        loc: Tuple[int, int],
        cache: Dict[str, CachedToken],
        buff: List[str],
        res: List[Token],
        cnt: Dict[str, CachedToken],
        char: str,
) -> None:
    # TODO: Optimize in the future
    # TODO: Add support for multiple SOT/EOT tokens
    # TODO: Add regex support
    # TODO: Add support for SOT content

    for tt, (current, end, tk) in cnt.items():
        if len(tk.type.sot) <= current + 1:
            end = True
        elif not end:
            current += 1

            if __handle_character(loc, cache, char, tk.type.sot[current], tt):
                continue

        if end:
            con, current = __handle_end_character(cache, buff, res, char, current, tk)

            if con:
                continue

        cache[tt] = (current, end, tk)


def __handle_eof(
        loc: Tuple[int, int],
        cache: Dict[str, CachedToken],
        res: List[Token]
) -> None:
    if cache:
        token = list(cache.values())[0][2]
        if token.type.eot != "\n":
            raise ExpectedEOT(
                loc,
                f"Expected end of token ({repr(token.type.eot)}) for {repr(token.type.represents)}"
            )

        res.append(token)


def tokenize(content: str) -> List[Token]:
    """
    Tokenize OODF syntax.

    Parameters:
    -----------
    content: :class:`str`
        A string in OODF syntax.

    Raises:
    -------
    InvalidSyntax
        The OODF syntax is invalid and could not be tokenized.
    ExpectedEOT
        No end of token was found.
    """

    registered_tokens: List[Token] = []
    __tkn_cache: Dict[str, CachedToken] = {}
    __end_buffer: List[str] = []

    __loc: Tuple[int, int] = (0, 0)

    for row, line in enumerate(content.splitlines(True)):
        for col, c in enumerate(line):
            __loc = (row, col)
            if __handle_token_cache(__loc, __tkn_cache, c):
                continue

            __lex_content(
                __loc,
                __tkn_cache,
                __end_buffer,
                registered_tokens,
                deepcopy(__tkn_cache),
                c
            )

    __handle_eof(__loc, __tkn_cache, registered_tokens)

    return registered_tokens
