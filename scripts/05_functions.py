"""
Module 05: Functions, Parameters, Arguments, and Return Values
============================================================

This module demonstrates modular software design in Python using functions:
- Function declaration and execution
- Positional vs. Keyword arguments
- Default argument values
- Functions returning values vs. displaying side effects
"""

def simple_greeting():
    """Demonstrates a simple function with no arguments or return value."""
    print("Hello! This is a simple greeting function.")


def greet_user(name: str, age: int = 18) -> str:
    """
    Greets a user with name and age parameters.
    Demonstrates default parameter values (age defaults to 18).
    """
    return f"User Profile -> Name: {name}, Age: {age}"


def check_palindrome_function(text: str) -> bool:
    """Reusable function to test if a string is a palindrome."""
    cleaned = text.lower()
    reversed_text = ""
    for i in range(len(cleaned) - 1, -1, -1):
        reversed_text += cleaned[i]
    return reversed_text == cleaned


def calculate_area(length: float, width: float) -> float:
    """Calculates rectangular area from length and width arguments."""
    return length * width


if __name__ == "__main__":
    print("--- Function Syntax & Execution ---")
    simple_greeting()

    # Calling with positional arguments
    print(greet_user("Akarsh", 23))

    # Calling with keyword arguments (order doesn't matter)
    print(greet_user(age=25, name="Nischal"))

    # Calling with default parameter
    print(greet_user("Alice"))

    # Testing reusable palindrome checker
    test_str1 = "NAMAN"
    test_str2 = "CURSOR"
    print(f"Is '{test_str1}' a palindrome?: {check_palindrome_function(test_str1)}")
    print(f"Is '{test_str2}' a palindrome?: {check_palindrome_function(test_str2)}")

    # Calculating area
    area = calculate_area(5.5, 4.0)
    print(f"Calculated Area (5.5 x 4.0): {area}")
