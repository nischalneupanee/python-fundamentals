"""
Module 03: Control Flow and Conditional Decision Logic in Python
===============================================================

This module demonstrates conditional logic using `if`, `elif`, and `else` statements
with real-world practical examples and utility functions.
"""

def classify_ice_cream(money: int) -> str:
    """Classifies dessert options based on budget."""
    if money == 10:
        return "Choco bar icecream"
    elif money == 20:
        return "Mango dolly"
    elif money == 30:
        return "Frosty"
    else:
        return "Waffle cone"


def compare_numbers(num1: int, num2: int) -> str:
    """Compares two integer values."""
    if num1 > num2:
        return f"{num1} is greater than {num2}"
    elif num2 > num1:
        return f"{num2} is greater than {num1}"
    else:
        return "Both numbers are equal"


def greet_by_gender(gender_char: str) -> str:
    """Returns a greeting based on gender input."""
    g = gender_char.upper()
    if g == 'M':
        return "Good morning SIR"
    elif g == 'F':
        return "Good morning MAM"
    else:
        return "Unidentified gender"


def is_even(num: int) -> bool:
    """Checks if a number is even."""
    return num % 2 == 0


def check_voting_eligibility(name: str, age: int) -> str:
    """Determines voter eligibility based on age threshold."""
    if age >= 18:
        return f"Hello {name}, you are eligible to vote."
    else:
        return f"Hello {name}, you are not eligible to vote."


def is_leap_year(year: int) -> bool:
    """
    Determines if a given year is a leap year.
    A year is a leap year if it is divisible by 4, except end-of-century years
    which must be divisible by 400.
    """
    if (year % 100 == 0 and year % 400 == 0) or (year % 100 != 0 and year % 4 == 0):
        return True
    else:
        return False


def classify_temperature(temp: float) -> str:
    """Categorizes temperature into qualitative weather descriptions."""
    if temp < 0:
        return "Freezing cold"
    elif 0 <= temp < 10:
        return "Very cold"
    elif 10 <= temp < 20:
        return "Cold"
    elif 20 <= temp < 30:
        return "Pleasant"
    elif 30 <= temp < 40:
        return "Hot"
    else:
        return "Extreme heat"


if __name__ == "__main__":
    print("--- Control Flow Examples ---")
    print(f"Budget $20 choice: {classify_ice_cream(20)}")
    print(f"Compare (15, 25): {compare_numbers(15, 25)}")
    print(f"Gender greeting ('M'): {greet_by_gender('M')}")
    print(f"Is 42 even?: {is_even(42)}")
    print(f"Voter Check ('Alice', 20): {check_voting_eligibility('Alice', 20)}")
    print(f"Is 2024 a leap year?: {is_leap_year(2024)}")
    print(f"Is 1900 a leap year?: {is_leap_year(1900)}")
    print(f"Temperature 25°C: {classify_temperature(25)}")
