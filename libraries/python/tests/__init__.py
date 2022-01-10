# Project is under an MIT-style license that can be found in the LICENSE file at the monorepo
# Monorepo: https://github.com/Arthurdw/oodf/libraries/python

"""
Test suites for the oodf library.
"""
from libraries.python.oodf import tokens

token_types = {
    t.represents: t for t in tokens
}
