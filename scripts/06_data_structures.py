"""
Module 06: Python Built-in Data Structures (Lists, Tuples, Sets, Dictionaries)
=============================================================================

This module demonstrates core data structures in Python:
- Lists: Operations, searching, sorting checks, statistics, second-largest element.
- Tuples: Immutability, indexing, counting, single-element syntax.
- Sets: Uniqueness, set operations, difference operators.
- Dictionaries: CRUD operations, merging, frequency counting, max frequency analysis.
"""

def demo_lists():
    print("--- 1. List Operations & Algorithms ---")
    numbers = [-45, 67, 12, -68, -69, 34]
    
    # Filtering positive and negative elements
    positive = [x for x in numbers if x >= 0]
    negative = [x for x in numbers if x < 0]
    print(f"Original List: {numbers}")
    print(f"Positive Elements: {positive}")
    print(f"Negative Elements: {negative}")

    # Average of list
    data = [12, 435, 67, 89, 23, 25, 69]
    avg = sum(data) / len(data)
    print(f"Average of {data}: {avg:.2f}")

    # Finding largest element and its index
    values = [12, 567, 43, 235, 347, 568, 45, 7]
    largest = values[0]
    largest_idx = 0
    for idx, val in enumerate(values):
        if val > largest:
            largest = val
            largest_idx = idx
    print(f"Largest in {values}: {largest} at index {largest_idx}")

    # Finding second largest element
    sample = [12, 16, 13, 19, 17]
    largest_val = float('-inf')
    second_largest = float('-inf')
    for num in sample:
        if num > largest_val:
            second_largest = largest_val
            largest_val = num
        elif num > second_largest and num != largest_val:
            second_largest = num
    print(f"In {sample} -> Largest: {largest_val}, Second Largest: {second_largest}")

    # Checking if list is sorted
    arr_sorted = [12, 13, 15, 16, 18]
    arr_unsorted = [12, 13, 18, 15, 16]
    
    def is_sorted(arr: list) -> bool:
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                return False
        return True

    print(f"Is {arr_sorted} sorted?: {is_sorted(arr_sorted)}")
    print(f"Is {arr_unsorted} sorted?: {is_sorted(arr_unsorted)}")


def demo_tuples():
    print("\n--- 2. Tuple Operations ---")
    tup = (1, 2, 3, 4, 5, 5, 5.5, "hello")
    print(f"Tuple content: {tup}")
    print(f"Count of 5 in tuple: {tup.count(5)}")
    
    # Single element tuple requirement (must include trailing comma)
    single_tup = (1,)
    not_a_tup = (1)
    print(f"type((1,)): {type(single_tup)} | type((1)): {type(not_a_tup)}")


def demo_sets():
    print("\n--- 3. Set Operations ---")
    set_a = {1, 2, 3, 4, 5}
    set_b = {4, 5, 6, 7, 8}
    print(f"Set A: {set_a}")
    print(f"Set B: {set_b}")

    # In-place difference
    difference = set_b - set_a
    print(f"Set B - Set A: {difference}")

    # Clearing a set
    temp_set = {8, 1, 2, 3, 4}
    temp_set.clear()
    print(f"Cleared set: {temp_set}")


def demo_dictionaries():
    print("\n--- 4. Dictionary Operations ---")
    d = {10: 100, 20: 200, 30: 300, 40: 400}
    d[10] = 150   # Updating value
    d[50] = 500   # Creating new key-value pair
    del d[30]     # Deleting key
    print(f"Modified Dictionary: {d}")
    print(f"Dictionary items: {list(d.items())}")

    # Merging and summing dictionaries
    d1 = {10: 100, 20: 200, 40: 300}
    d2 = {40: 400, 50: 500, 60: 600}
    merged = d1.copy()
    for k, v in d2.items():
        merged[k] = merged.get(k, 0) + v
    print(f"Combined Key Values (d1 + d2): {merged}")

    # Frequency Counter & Most Frequent Element
    elements = [1, 1, 1, 2, 2, 2, 3, 3, 3, 3, 3, 3, 4, 4, 4, 5, 5]
    freq = {}
    for el in elements:
        freq[el] = freq.get(el, 0) + 1

    most_frequent = max(freq, key=freq.get)
    print(f"Frequency dict: {freq}")
    print(f"Most frequent element: {most_frequent} (occurred {freq[most_frequent]} times)")


if __name__ == "__main__":
    demo_lists()
    demo_tuples()
    demo_sets()
    demo_dictionaries()
