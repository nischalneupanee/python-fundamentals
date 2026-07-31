"""
Module 01: Syntax, Comments, and Variable Naming Conventions in Python
================================================----------------======

This module demonstrates fundamental Python syntax concepts including:
- Single-line and multi-line comments / docstrings
- Variable assignment and dynamic typing
- Standard Python variable naming conventions (snake_case, camelCase, PascalCase)
"""

# ==============================================================================
# 1. COMMENTS AND DOCSTRINGS
# ==============================================================================

# This is a single-line comment. Python ignores anything after '#' on the line.

"""
This is a multi-line string used as a module or function docstring.
Docstrings document what code blocks, functions, or classes do.
"""


# ==============================================================================
# 2. VARIABLE ASSIGNMENT
# ==============================================================================

author_name = "Nischal Neupane"
user_role = "Developer"

print(f"Author: {author_name}")
print(f"Role: {user_role}")


# ==============================================================================
# 3. NAMING CONVENTIONS
# ==============================================================================

# Snake Case (PEP 8 recommended for variable and function names)
code_writer = "Nischal"

# Camel Case (Common in other languages like JavaScript)
codeWriter = "Nischal"

# Pascal Case (PEP 8 recommended for Class names)
CodeWriter = "Nischal"


# ==============================================================================
# 4. VARIABLE NAMING RULES & SYNTAX NOTES
# ==============================================================================
# - Variable names must start with a letter (a-z, A-Z) or an underscore (_).
# - Variable names CANNOT start with a digit (e.g., `1ad = 34` raises a SyntaxError).
# - Variable names are case-sensitive (`author_name` vs `Author_Name`).

if __name__ == "__main__":
    print("\n--- Syntax & Variables Module Loaded Successfully ---")
    print(f"Snake case variable: code_writer = '{code_writer}'")
    print(f"Camel case variable: codeWriter = '{codeWriter}'")
    print(f"Pascal case variable: CodeWriter = '{CodeWriter}'")
