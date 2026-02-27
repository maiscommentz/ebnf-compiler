# SPDX-FileCopyrightText: 2026 Filipe Casimiro Ferreira <pro.maiscommentz@gmail.com>
#
# SPDX-License-Identifier: MIT

"""
EBNF Tokens
"""

from enum import Enum, auto


class Token(Enum):
    IDENT = auto()
    LITERAL = auto()
    LPAREN = auto()
    LBRAK = auto()
    LBRACE = auto()
    BAR = auto()
    EQL = auto()
    RPAREN = auto()
    RBRAK = auto()
    RBRACE = auto()
    PERIOD = auto()
    OTHER = auto()
    EOF = auto()
