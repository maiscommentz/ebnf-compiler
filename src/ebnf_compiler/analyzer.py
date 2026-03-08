# SPDX-FileCopyrightText: 2026 Filipe Casimiro Ferreira <pro.maiscommentz@gmail.com>
#
# SPDX-License-Identifier: MIT

"""
AST Analyzer for identifying terminal and non-terminal symbols.
"""

from . import ast


class Analyzer:
    def __init__(self, syntax_tree: ast.Syntax):
        self.syntax_tree = syntax_tree
        self.defined_symbols: set[str] = set()
        self.used_symbols: set[str] = set()

    def analyze(self) -> None:
        for prod in self.syntax_tree.production:
            self.defined_symbols.add(prod.identifier.value)
            self._visit_expression(prod.expression)

    def _visit_expression(self, expr: ast.Expression) -> None:
        for term in expr.terms:
            for factor in term.factors:
                self._visit_factor(factor)

    def _visit_factor(self, factor: ast.Factor) -> None:
        if isinstance(factor, ast.Identifier):
            self.used_symbols.add(factor.value)
        elif isinstance(factor, ast.Expression):
            self._visit_expression(factor)
        elif isinstance(factor, (ast.Option, ast.Repetition)):
            self._visit_expression(factor.expr)
        elif isinstance(factor, ast.Literal):
            pass

    @property
    def non_terminals(self) -> list[str]:
        return sorted(list(self.defined_symbols))

    @property
    def terminals(self) -> list[str]:
        return sorted(list(self.used_symbols - self.defined_symbols))
