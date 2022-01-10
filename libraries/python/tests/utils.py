# Project is under an MIT-style license that can be found in the LICENSE file at the monorepo
# Monorepo: https://github.com/Arthurdw/oodf/libraries/python

from __future__ import annotations

__cached = {}


def __read_file(name, path: str, cache: bool = True) -> str:
    with open(path, "r") as f:
        sample = f.read()

        if cache:
            __cached[name] = sample

        return sample


def get_sample(name: str, cache: bool = True) -> str:
    """
    Read a sample file and return it for test assertion.

    Parameters:
    -----------
    name: :class:`str`
        name of the sample file
    cache: :class:`bool`
        cache the sample file in memory
    """

    if cache and (cached := __cached.get(name)):
        return cached

    try:
        return __read_file(name, f"../../../examples/{name}.oodf", cache)
    except FileNotFoundError:
        return __read_file(name, f"./examples/{name}.oodf", cache)
