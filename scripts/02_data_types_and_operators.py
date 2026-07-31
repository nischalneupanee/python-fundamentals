"""
Module 02: Primitive Data Types and Operators in Python
======================================================

This module demonstrates:
- Primitive data types (int, float, complex, str, bool)
- Dynamic type checking with `type()`
- Arithmetic, Compound Assignment, Comparison, and Logical Operators
- Character ASCII conversions using `ord()`
"""

def demo_data_types():
    print("--- 1. Primitive Data Types ---")
    integer_val = -34
    float_val = 56.8
    division_result = 12 / 3  # Division produces a float
    complex_val = 34j         # Complex number
    string_val = "Hello Python 3.12!"
    bool_val = True

    print(f"Integer: {integer_val} | Type: {type(integer_val)}")
    print(f"Float: {float_val} | Type: {type(float_val)}")
    print(f"Division Result (12/3): {division_result} | Type: {type(division_result)}")
    print(f"Complex: {complex_val} | Type: {type(complex_val)}")
    print(f"String: {string_val} | Type: {type(string_val)}")
    print(f"Boolean: {bool_val} | Type: {type(bool_val)}")


def demo_operators():
    print("\n--- 2. Arithmetic Operators ---")
    a, b = 5, 32
    print(f"a = {a}, b = {b}")
    print(f"Addition (a + b): {a + b}")
    print(f"Subtraction (b - a): {b - a}")
    print(f"Multiplication (a * b): {a * b}")
    print(f"True Division (b / a): {b / a}")
    print(f"Floor Division (b // a): {b // a}")
    print(f"Modulus (b % a): {b % a}")
    print(f"Exponentiation (a ** 3): {a ** 3}")

    print("\n--- 3. Compound Assignment Operators ---")
    val = 20
    print(f"Initial val: {val}")
    val += 20  # 40
    val *= 2   # 80
    val -= 10  # 70
    val //= 3  # 23
    print(f"Final val after compound operations: {val}")

    print("\n--- 4. Comparison Operators ---")
    x, y = 12.1, 12
    print(f"x = {x}, y = {y}")
    print(f"x == y: {x == y}")
    print(f"x != y: {x != y}")
    print(f"x > y: {x > y}")
    print(f"23 >= 23: {23 >= 23}")

    print("\n--- 5. String Comparison & ASCII Values ---")
    print(f"ord('A'): {ord('A')}, ord('B'): {ord('B')}")
    print(f"'ABC' > 'ACD': {'ABC' > 'ACD'}")

    print("\n--- 6. Logical Operators ---")
    cond1 = (12 < 20) and (34 == 34)  # True
    cond2 = (12 != 12) or (10 > 5)     # True
    cond3 = not (12 == 12)             # False
    print(f"(12 < 20) and (34 == 34): {cond1}")
    print(f"(12 != 12) or (10 > 5): {cond2}")
    print(f"not (12 == 12): {cond3}")


if __name__ == "__main__":
    demo_data_types()
    demo_operators()
