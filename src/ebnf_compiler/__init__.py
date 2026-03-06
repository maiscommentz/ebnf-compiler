# SPDX-FileCopyrightText: 2026 Filipe Casimiro Ferreira <pro.maiscommentz@gmail.com>
#
# SPDX-License-Identifier: MIT

"""
EBNF Compiler
"""

import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Annotated

import typer
from loguru import logger
from rich.console import Console
from rich.panel import Panel
from rich.pretty import Pretty

from . import ast
from .parser import Parser
from .scanner import Scanner

console = Console()
app = typer.Typer()


@dataclass
class Compiler:
    scanner: Scanner
    parser: Parser

    def ast(self) -> ast.Syntax | None:
        try:
            return self.parser.parse()
        except Exception as e:
            print(f"{e}")
            return None


@app.command(context_settings={"ignore_unknown_options": True})
def main(
    source: Annotated[Path, typer.Argument()],
    debug: bool = False,
    show_tree: bool = True,
):

    logger.remove()
    if debug:
        logger.add(sys.stdout, level="DEBUG")
    else:
        logger.add(sys.stdout, level="INFO")

    scanner = Scanner()
    scanner.open(source)
    parser = Parser(scanner=scanner)

    compiler = Compiler(scanner=scanner, parser=parser)
    ast_ = compiler.ast()

    if ast_ is None:
        console.print("[red]Compilation failed[/red]")
        return

    console.print(Panel(ast_.rich(), title="Code"))

    if show_tree:
        console.print(Panel(Pretty(ast_, indent_size=2), title="Syntax Tree"))


if __name__ == "__main__":
    app()
