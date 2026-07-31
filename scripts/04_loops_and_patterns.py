"""
Module 04: Iteration, Loops, Algorithmic Problems, and Pattern Generation
========================================================================

This module covers:
- `for` and `while` loops, `range()`, and `else` clauses on loops
- Mathematical algorithms (Factorial, Prime check, Perfect numbers, Strong numbers)
- String & Integer reversals and Palindrome detection
- Character breakdown analysis
- Geometric Star Patterns (Pyramid, Diamond)
"""

def generate_multiplication_table(n: int) -> list[str]:
    """Generates multiplication table strings for integer n from 1 to 10."""
    return [f"{n} * {i} = {n * i}" for i in range(1, 11)]


def calculate_sum(n: int) -> int:
    """Calculates sum of natural numbers from 1 to n."""
    total = 0
    for i in range(1, n + 1):
        total += i
    return total


def calculate_factorial(n: int) -> int:
    """Calculates n! (factorial of n)."""
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact


def sum_even_odd(n: int) -> tuple[int, int]:
    """Returns tuple of (even_sum, odd_sum) up to n."""
    even_sum, odd_sum = 0, 0
    for i in range(1, n + 1):
        if i % 2 == 0:
            even_sum += i
        else:
            odd_sum += i
    return even_sum, odd_sum


def get_factors(n: int) -> list[int]:
    """Returns list of all factors of n."""
    return [i for i in range(1, n + 1) if n % i == 0]


def is_perfect_number(n: int) -> bool:
    """A number is perfect if the sum of its proper divisors equals the number."""
    if n <= 0:
        return False
    divisor_sum = sum(i for i in range(1, n) if n % i == 0)
    return divisor_sum == n


def is_prime(n: int) -> bool:
    """Checks if n is a prime number."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def find_primes_in_range(start: int, end: int) -> list[int]:
    """Finds all prime numbers in the range [start, end]."""
    return [num for num in range(start, end + 1) if is_prime(num)]


def is_string_palindrome(s: str) -> bool:
    """Checks if a string reads the same backwards."""
    cleaned = s.upper()
    return cleaned == cleaned[::-1]


def is_number_palindrome(num: int) -> bool:
    """Reverses an integer mathematically and checks if it's a palindrome."""
    temp = abs(num)
    rev = 0
    while temp > 0:
        rev = rev * 10 + (temp % 10)
        temp //= 10
    return rev == abs(num)


def analyze_string_characters(text: str) -> dict[str, int]:
    """Counts alphabetic, digit, and special characters in a string."""
    counts = {"digits": 0, "alphabets": 0, "special": 0}
    for char in text:
        if char.isdigit():
            counts["digits"] += 1
        elif char.isalpha():
            counts["alphabets"] += 1
        else:
            counts["special"] += 1
    return counts


def is_strong_number(num: int) -> bool:
    """
    A number is strong if the sum of the factorials of its digits equals the number.
    Example: 145 = 1! + 4! + 5! = 1 + 24 + 120 = 145.
    """
    temp = num
    total_sum = 0
    while temp > 0:
        digit = temp % 10
        total_sum += calculate_factorial(digit)
        temp //= 10
    return total_sum == num


def generate_diamond_pattern(rows: int) -> list[str]:
    """Generates a diamond star pattern as a list of string lines."""
    lines = []
    # Upper pyramid
    for i in range(1, rows + 1):
        lines.append(" " * (rows - i) + "* " * i)
    # Lower inverted pyramid
    for i in range(rows - 1, 0, -1):
        lines.append(" " * (rows - i) + "* " * i)
    return lines


if __name__ == "__main__":
    print("--- Loops & Math Algorithms ---")
    print(f"Factorial of 5: {calculate_factorial(5)}")
    print(f"Factors of 28: {get_factors(28)}")
    print(f"Is 28 a perfect number?: {is_perfect_number(28)}")
    print(f"Is 17 prime?: {is_prime(17)}")
    print(f"Primes between 2 and 20: {find_primes_in_range(2, 20)}")
    print(f"Is 'NAMAN' a palindrome?: {is_string_palindrome('NAMAN')}")
    print(f"Is 12321 a palindrome number?: {is_number_palindrome(12321)}")
    print(f"String analysis of 'Py3.12!': {analyze_string_characters('Py3.12!')}")
    print(f"Is 145 a strong number?: {is_strong_number(145)}")

    print("\n--- Diamond Star Pattern (3 rows) ---")
    for line in generate_diamond_pattern(3):
        print(line)
