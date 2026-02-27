# SPDX-FileCopyrightText: 2026 Filipe Casimiro Ferreira <filipe.casimiro@edu.hefr.ch>
#
# SPDX-License-Identifier: Apache-2.0 OR MIT

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
