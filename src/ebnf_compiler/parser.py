# SPDX-FileCopyrightText: 2026 Filipe Casimiro Ferreira <pro.maiscommentz@gmail.com>
#
# SPDX-License-Identifier: MIT

"""
EBNF Parser
"""

from dataclasses import dataclass

from loguru import logger

from . import ast
from .scanner import Scanner
from .tokens import Token


@dataclass
class Parser:
    scanner: Scanner
    has_error: bool = False

    def raise_error(self, msg: str) -> None:
        self.has_error = True
        self.scanner.print_error(msg)
        raise Exception(msg)

    def raise_expected_error(self, expected: Token):
        self.raise_error(f"Expected '{expected}', but got '{self.scanner.sym}'")

    def factor(self) -> ast.Factor:
        logger.debug("Factor")
        sym = self.scanner.sym
        if sym == Token.IDENT:
            val = self.scanner.value
            self.scanner.get_next_symbol()
            return ast.Identifier(value=val)
        elif sym == Token.LITERAL:
            val = self.scanner.value
            self.scanner.get_next_symbol()
            return ast.Literal(value=val)
        elif sym == Token.LPAREN:
            self.scanner.get_next_symbol()
            expr = self.expression()
            expr.paren = True
            if self.scanner.sym != Token.RPAREN:
                self.raise_expected_error(Token.RPAREN)
            self.scanner.get_next_symbol()
            return expr
        elif sym == Token.LBRAK:
            self.scanner.get_next_symbol()
            expr = self.expression()
            if self.scanner.sym != Token.RBRAK:
                self.raise_expected_error(Token.RBRAK)
            self.scanner.get_next_symbol()
            return ast.Option(expr=expr)
        elif sym == Token.LBRACE:
            self.scanner.get_next_symbol()
            expr = self.expression()
            if self.scanner.sym != Token.RBRACE:
                self.raise_expected_error(Token.RBRACE)
            self.scanner.get_next_symbol()
            return ast.Repetition(expr=expr)
        else:
            self.raise_error(
                f"Expected identifier, literal, (', '['. or '{{' got {sym}"
            )
            raise Exception("Unexpected symbol")

    def term(self) -> ast.Term:
        logger.debug("Term")
        factors = []
        factors.append(self.factor())

        while self.scanner.sym in (
            Token.IDENT,
            Token.LITERAL,
            Token.LPAREN,
            Token.LBRAK,
            Token.LBRACE,
        ):
            factors.append(self.factor())
        return ast.Term(factors=factors)

    def expression(self) -> ast.Expression:
        logger.debug("Expression")
        terms = []
        terms.append(self.term())
        while self.scanner.sym == Token.BAR:
            self.scanner.get_next_symbol()
            terms.append(self.term())
        return ast.Expression(terms=terms)

    def production(self) -> ast.Production:
        logger.debug("Production")
        if self.scanner.sym != Token.IDENT:
            self.raise_expected_error(Token.IDENT)
        ident = ast.Identifier(value=self.scanner.value)
        self.scanner.get_next_symbol()
        if self.scanner.sym != Token.EQL:
            self.raise_expected_error(Token.EQL)
        self.scanner.get_next_symbol()
        expr = self.expression()
        if self.scanner.sym != Token.PERIOD:
            self.raise_expected_error(Token.PERIOD)
        self.scanner.get_next_symbol()
        return ast.Production(identifier=ident, expression=expr)

    def syntax(self) -> ast.Syntax:
        logger.debug("Syntax")
        productions = []
        while self.scanner.sym != Token.EOF:
            if self.scanner.sym != Token.IDENT:
                self.raise_expected_error(Token.IDENT)
            productions.append(self.production())
        return ast.Syntax(production=productions)

    def parse(self) -> ast.Syntax:
        logger.debug("Parsing")
        self.scanner.get_next_symbol()
        return self.syntax()
