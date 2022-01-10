# Project is under an MIT-style license that can be found in the LICENSE file at the monorepo
# Monorepo: https://github.com/Arthurdw/oodf/libraries/python

from __future__ import annotations

from .core import tokenize, transpile


def load(content: str) -> dict:
    """
    Load/parse an oodf string into a python dictionary.

    Parameters:
    -----------
    content: :class:`str`
        The oodf string to parse.

    Returns:
    --------
    :class:`dict`
        The parsed oodf dictionary.
    """
    return transpile(tokenize(content))
