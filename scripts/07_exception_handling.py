"""
Module 07: Exception Handling and Error Control Flow in Python
=============================================================

This module demonstrates error handling strategies in Python:
- Catching exceptions using `try-except`
- Executing code on success using `else`
- Guaranteed cleanup using `finally`
- Raising custom exceptions using `raise`
"""

def safe_division(numerator: float, denominator: float) -> float | None:
    """Demonstrates complete try-except-else-finally handling."""
    print(f"\nAttempting division: {numerator} / {denominator}")
    try:
        result = numerator / denominator
    except ZeroDivisionError as err:
        print(f"[EXCEPT] Caught ZeroDivisionError: {err}")
        return None
    except TypeError as err:
        print(f"[EXCEPT] Caught TypeError: {err}")
        return None
    else:
        print(f"[ELSE] Division executed successfully! Result = {result}")
        return result
    finally:
        print("[FINALLY] Cleanup step: Division operation completed.")


def validate_user_age(age: int) -> bool:
    """Demonstrates raising a custom ValueError if validation criteria fail."""
    print(f"\nValidating age input: {age}")
    try:
        if age < 10 or age > 18:
            raise ValueError("Age must be strictly between 10 and 18.")
        else:
            print("Validation successful: Welcome to the youth club!")
            return True
    except ValueError as err:
        print(f"[EXCEPT] Age Validation Failed: {err}")
        return False


if __name__ == "__main__":
    print("--- Exception Handling Demonstrations ---")
    
    # 1. Successful division
    safe_division(10, 2)

    # 2. Division by zero
    safe_division(10, 0)

    # 3. Custom exception validation - valid input
    validate_user_age(15)

    # 4. Custom exception validation - invalid input
    validate_user_age(22)
