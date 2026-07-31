# 🐍 Python Fundamentals: Master Study & Reference Guide

[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Jupyter Notebooks](https://img.shields.io/badge/Jupyter-Interactive%20Notebooks-orange.svg)](notebooks/)
[![Code Style: PEP 8](https://img.shields.io/badge/code%20style-PEP%208-brightgreen.svg)](https://peps.python.org/pep-0008/)

Welcome to the **Python Fundamentals** repository — a clean, structured, and comprehensive guide designed to master Python from syntax basics to object-oriented programming and advanced features.

This repository serves as both an **interactive tutorial suite** (via Jupyter Notebooks) and a **runnable reference codebase** (via clean Python scripts).

---

## 📚 Table of Contents & Learning Modules

| # | Topic | Notebook (`.ipynb`) | Source Script (`.py`) | Key Concepts Covered |
|---|-------|----------------------|-----------------------|----------------------|
| **01** | **Syntax & Variables** | [Notebook](notebooks/01_syntax_and_variables.ipynb) | [Script](scripts/01_syntax_and_variables.py) | Single/multi-line comments, docstrings, variable naming rules, `snake_case` / `camelCase` / `PascalCase` |
| **02** | **Data Types & Operators** | [Notebook](notebooks/02_data_types_and_operators.ipynb) | [Script](scripts/02_data_types_and_operators.py) | Primitive types (`int`, `float`, `complex`, `str`, `bool`), dynamic typing, arithmetic, assignment, logical operators, ASCII `ord()` |
| **03** | **Control Flow** | [Notebook](notebooks/03_control_flow.ipynb) | [Script](scripts/03_control_flow.py) | `if`/`elif`/`else` logic, leap year checker, temperature classification, voter eligibility, decision trees |
| **04** | **Loops & Patterns** | [Notebook](notebooks/04_loops_and_patterns.ipynb) | [Script](scripts/04_loops_and_patterns.py) | `for` & `while` loops, loop `else`, prime numbers, factorials, perfect numbers, palindromes, strong numbers, diamond star patterns |
| **05** | **Functions** | [Notebook](notebooks/05_functions.ipynb) | [Script](scripts/05_functions.py) | Function signatures, positional vs keyword arguments, default parameters, return values vs side-effects |
| **06** | **Data Structures** | [Notebook](notebooks/06_data_structures.ipynb) | [Script](scripts/06_data_structures.py) | **Lists**: sorting checks, second largest element; **Tuples**: immutability; **Sets**: difference operations; **Dicts**: merging, frequency counting |
| **07** | **Exception Handling** | [Notebook](notebooks/07_exception_handling.ipynb) | [Script](scripts/07_exception_handling.py) | `try`/`except`/`else`/`finally` blocks, catching built-in errors, raising custom exceptions with `raise ValueError` |
| **08** | **File Handling** | [Notebook](notebooks/08_file_handling.ipynb) | [Script](scripts/08_file_handling.py) | File I/O modes (`'r'`, `'w'`, `'a'`), clean resource management using `with open(...)` context managers |
| **09** | **Object-Oriented Programming** | [Notebook](notebooks/09_object_oriented_programming.ipynb) | [Script](scripts/09_object_oriented_programming.py) | Classes, `__init__`, instance vs class methods (`@classmethod`, `@staticmethod`), inheritance (`super()`), encapsulation (`__private`), abstraction (`ABC`), dunder methods (`__str__`, `__add__`), `@property` |
| **10** | **Advanced Python** | [Notebook](notebooks/10_advanced_python.ipynb) | [Script](scripts/10_advanced_python.py) | Custom decorators (`@logging_decorator`), `*args` & `**kwargs`, dictionary comprehensions, `map()` & `filter()` |

---

## 🚀 Quick Start

### 1. Prerequisites
Ensure you have **Python 3.10+** installed:
```bash
python3 --version
```

### 2. Clone Repository
```bash
git clone https://github.com/nischalneupanee/python-fundamentals.git
cd python-fundamentals
```

### 3. Run Standalone Scripts
You can execute any of the Python script modules directly from your terminal:
```bash
python3 scripts/01_syntax_and_variables.py
python3 scripts/04_loops_and_patterns.py
python3 scripts/09_object_oriented_programming.py
```

### 4. Launch Interactive Notebooks
If you prefer studying interactively with Jupyter:
```bash
pip install jupyterlab
jupyter lab
```
Then open any notebook inside the `notebooks/` directory.

---

## 💡 Algorithmic Highlights Included

- **Strong Numbers**: Checks if the sum of factorials of digits equals the number (e.g., $145 = 1! + 4! + 5!$).
- **Diamond Star Pattern**: Generates symmetric geometric star patterns.
- **Second Largest Element**: Linear time algorithm to extract second maximum without sorting.
- **Frequency Counter**: Dictionary-based $O(N)$ frequency analysis to identify peak occurrences.
- **Abstract Base Classes**: Enforces Interface contracts using Python's `abc` module.

---

## 📜 License

Distributed under the MIT License. See [LICENSE](LICENSE) for details.

---

## 👨‍💻 Author

Developed and maintained by **Nischal Neupane**.
