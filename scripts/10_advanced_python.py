"""
Module 10: Advanced Python Techniques (Decorators, *args/**kwargs, Comprehensions, map/filter)
===========================================================================================

This module demonstrates advanced language features in Python:
- Custom Decorators & Higher-Order Functions
- Variable-length arguments (`*args` and `**kwargs`)
- Dictionary Comprehensions
- Functional programming tools (`map`, `filter`)
"""

# ==============================================================================
# 1. DECORATORS & HIGHER-ORDER FUNCTIONS
# ==============================================================================

def logging_decorator(func):
    """Decorator that prints logs before and after function execution."""
    def wrapper(*args, **kwargs):
        print(f"[DECORATOR LOG] Executing '{func.__name__}' with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"[DECORATOR LOG] '{func.__name__}' completed. Output: {result}")
        return result
    return wrapper


@logging_decorator
def add_numbers(a: int, b: int) -> int:
    """Calculates sum of two integers."""
    return a + b


# ==============================================================================
# 2. VARIABLE-LENGTH KEYWORD ARGUMENTS (**kwargs)
# ==============================================================================

def display_user_profile(**kwargs) -> dict:
    """Processes arbitrary keyword arguments into a structured profile dictionary."""
    print("\n--- User Profile Attributes ---")
    for key, value in kwargs.items():
        print(f"  {key.capitalize()}: {value}")
    return kwargs


# ==============================================================================
# 3. DICTIONARY & LIST COMPREHENSIONS
# ==============================================================================

def demo_comprehensions():
    print("\n--- Dictionary & List Comprehensions ---")
    # Generating a dictionary of number squares
    square_dict = {i: i**2 for i in range(1, 6)}
    print(f"Square Dictionary (1-5): {square_dict}")

    # Conditional dict comprehension
    even_squares = {i: i**2 for i in range(1, 10) if i % 2 == 0}
    print(f"Even Squares Dictionary (1-9): {even_squares}")


# ==============================================================================
# 4. FUNCTIONAL PROGRAMMING: map() & filter()
# ==============================================================================

def demo_functional_tools():
    print("\n--- Functional Tools: map() and filter() ---")
    nums = [1, 2, 3, 4, 5]

    # map: double each element
    doubled = list(map(lambda x: x * 2, nums))
    print(f"Original: {nums} -> Doubled via map(): {doubled}")

    # filter: keep only even elements
    evens = list(filter(lambda x: x % 2 == 0, nums))
    print(f"Original: {nums} -> Evens via filter(): {evens}")


if __name__ == "__main__":
    print("--- Advanced Python Features ---")
    # Test decorator
    add_numbers(12, 67)

    # Test kwargs
    display_user_profile(name="Akarsh", age=23, designation="AI/ML Engineer", country="Nepal")

    # Test comprehensions & functional tools
    demo_comprehensions()
    demo_functional_tools()
