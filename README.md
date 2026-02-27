# EBNF Compiler

EBNF Compiler is a compiler for the EBNF (Extended Backus-Naur Form) notation. This project was developed as part of the "Compiler Construction" course at HEIA-FR, Switzerland.

📝 **Access the documentation online:** [https://maiscommentz.github.io/ebnf-compiler/](https://maiscommentz.github.io/ebnf-compiler/)


## 🛠️ Technologies
![Python](https://img.shields.io/badge/-Python-4584B6?logo=python&logoColor=white&style=for-the-badge)
![uv](https://img.shields.io/badge/-uv-4584B6?logo=uv&logoColor=white&style=for-the-badge)
![Pytest](https://img.shields.io/badge/-Pytest-4584B6?logo=pytest&logoColor=white&style=for-the-badge)
![Ruff](https://img.shields.io/badge/-Ruff-4584B6?logo=ruff&logoColor=white&style=for-the-badge)
![Pyright](https://img.shields.io/badge/-Pyright-4584B6?logo=pyright&logoColor=white&style=for-the-badge)
![MyPy](https://img.shields.io/badge/-MyPy-4584B6?logo=mypy&logoColor=white&style=for-the-badge)
![Sphinx](https://img.shields.io/badge/-Sphinx-4584B6?logo=sphinx&logoColor=white&style=for-the-badge)
![Black](https://img.shields.io/badge/-Black-4584B6?logo=black&logoColor=white&style=for-the-badge)
![REUSE](https://img.shields.io/badge/-REUSE-4584B6?logo=reuse&logoColor=white&style=for-the-badge)
## ✨ Key Features

- **Lexical Analysis (Scanner)**: Tokenizes EBNF grammars into meaningful symbols.
- **Syntax Analysis (Parser)**: Validates grammars against standard EBNF rules.
- **Modern Python Architecture**: Built with Python 3.12+, fully typed using `pyright` and `mypy`.
- **Command-Line Interface**: Easy-to-use CLI built with Typer and Rich.

## 📁 Project Structure

```text
.
├── .github/workflows/              # GitHub Actions CI/CD pipelines
├── docs/                           # Sphinx documentation (deployed to GH Pages)
├── LICENSES/                       # SPDX License files (MIT)
├── src/ebnf_compiler/              # Core compiler source code
├── tests/                          # Pytest test suite
├── examples/                       # Example EBNF grammar files
├── .gitignore                      # Git ignore files
├── .pre-commit-config.yaml         # Pre-commit configuration
├── .python-version                 # Python version file
├── pyproject.toml                  # Python build & dependency configuration (uv)
├── README.md                       # This file
└── REUSE.toml                      # REUSE specification
```

## 🚀 Installation and Usage

This project uses [uv](https://github.com/astral-sh/uv) as its modern and ultra-fast Python package manager.

### Prerequisites

- [Python 3.12](https://www.python.org/downloads/) or higher
- [uv](https://docs.astral.sh/uv/)

### Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/maiscommentz/ebnf-compiler.git
   cd ebnf-compiler
   ```

2. **Install dependencies:**
   ```bash
   uv sync
   ```

### Run the compiler

Once the environment is synced, you can use the EBNF compiler via its CLI:

```bash
uv run ebnf-compiler --help
```

You can point the compiler to a grammar file (like those in the `examples/` directory):

```bash
uv run ebnf-compiler examples/basic.ebnf
```

## 🛠️ Development Guide

We encourage high code quality standards. This project enforces styling and typing checks using `pre-commit`.

### Running Tests

Execute the automated test suite using pytest:
```bash
uv run pytest
```

### Static Analysis & Formatting

Ensure your code meets the quality standards (Black, Ruff, Pyright, MyPy) by running pre-commit:
```bash
uv run pre-commit run --all-files
```

### Building Documentation

To compile the Sphinx documentation locally:
```bash
cd docs
uv run make html
```
The built pages will be available in `docs/_build/html/`.

## 🔄 Continuous Integration (CI/CD)

The repository relies on a complete **GitHub Actions** pipeline configured in `.github/workflows/workflow.yml`. It automatically handles:

1. **Validation**: Enforces `pre-commit` (formatting, linting, type-checking).
2. **Testing**: Runs the `pytest` suite across the codebase automatically.
3. **Documentation**: Builds the Sphinx docs and deploys them directly to **GitHub Pages** (on the main branch).
4. **Releases**: Builds Python distribution packages when a new GitHub Release is published.

## 📄 License

This project complies with the [REUSE](https://reuse.software/) specification. 
The source code is licensed under the **MIT License**. See the `LICENSES/MIT.txt` file for more details.

© 2026 Filipe Casimiro Ferreira <pro.maiscommentz@gmail.com>
