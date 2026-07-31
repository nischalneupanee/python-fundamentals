"""
Module 08: File I/O Operations and Context Managers in Python
============================================================

This module demonstrates:
- File opening modes ('w' for write, 'a' for append, 'r' for read)
- Modern resource management using `with open(...)` context managers
- Handling file read/write operations safely
"""

import os
from pathlib import Path

def demo_file_operations():
    # Use a safe path within workspace/tmp directory for demonstration
    target_dir = Path(__file__).parent / "temp_output"
    target_dir.mkdir(exist_ok=True)
    file_path = target_dir / "sample_log.txt"

    print(f"Working with target file: {file_path}")

    # 1. Writing to a file ('w' mode overwrites existing content)
    with open(file_path, "w", encoding="utf-8") as f:
        f.write("Line 1: Initializing Python Fundamentals file log.\n")
        f.write("Line 2: Demonstration of file writing mode.\n")

    print("[SUCCESS] Initial file created and written.")

    # 2. Appending to a file ('a' mode adds to the end)
    with open(file_path, "a", encoding="utf-8") as f:
        f.write("Line 3: Appended content inside the file.\n")

    print("[SUCCESS] New content appended.")

    # 3. Reading from a file ('r' mode)
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    print("\n--- File Content Output ---")
    print(content)

    # Clean up temporary test file
    if file_path.exists():
        file_path.unlink()
        target_dir.rmdir()
        print("[CLEANUP] Temporary test directory and file removed.")


if __name__ == "__main__":
    demo_file_operations()
