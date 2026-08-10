# Topic: File Handling - Reading Files (Month 2: Core Python)
#
# Key Concepts:
# 1. Opening a file for reading: `open(filename, 'r')` (or default mode)
# 2. Reading methods:
#    - `file.read()`       : Reads the ENTIRE file content into a single string.
#    - `file.readline()`   : Reads a single line at a time.
#    - `file.readlines()`  : Reads ALL lines into a LIST of strings.
#    - `for line in file:` : Iterates line by line (best practice for large files!).
# 3. Cleaning strings:
#    - Lines read from files include trailing newline characters `\n`.
#    - Use `line.strip()` to remove leading/trailing whitespace and newlines.

# ----------------------------------------------------
# Demonstration Code:
# ----------------------------------------------------


# file_path = "02_python_core/sample_notes.txt"

# print("--- Reading File (Line by Line) ---")
# with open(file_path, "r") as file:
#     for line_no, line in enumerate(file, 1):
#         print(f"Line {line_no}: {line.strip()}")

# print("\n--- Reading File into a List with readlines() ---")
# with open(file_path, "r") as file:
#     lines = file.readlines()
#     print(f"Total lines read: {len(lines)}")
#     print("Raw list:", lines)


# ====================================================
# YOUR PRACTICE TASK:
# ====================================================
# Problem Statement:
# Read the goals saved in `02_python_core/my_goals.txt` and display them formatted neatly.
#
# Steps to complete:
# 1. Open `02_python_core/my_goals.txt` in read mode ('r').
# 2. Loop through each line and print it out cleaned with `.strip()`.
# 3. Count how many total goals were found in the file and print:
#    "Total goals loaded: X"
#
# Write your solution code below:

# Define the file path of the file we want to read
file_path = "02_python_core/02_read/read_goals.txt"

# Open the file in Read mode ('r') using 'with' (automatically closes file when done)
with open(file_path, "r") as file:
    # Use enumerate(file, 1) to get line_no (starting at 1) and line text
    for line_no, line in enumerate(file, 1):
        # .strip() removes trailing newline '\n' characters
        print(line.strip())

# Print total lines read using line_no (which holds the final line count)
print(f"Total goals read: {line_no}")


# ====================================================
# SUMMARY NOTES FOR REVISION:
# ====================================================
# 1. READ METHODS IN PYTHON:
#    - file.read()       : Reads entire file as 1 single string (High RAM usage for big files).
#    - file.readline()   : Reads 1 single line at a time as a string.
#    - file.readlines()  : Reads all lines into a LIST of strings.
#    - for line in file: : Loops line-by-line efficiently (BEST PRACTICE).
#
# 2. `enumerate(file, 1)` EXPLAINED:
#    - Automatically tracks the line counter while looping.
#    - First argument (`file`): The file iterator.
#    - Second argument (`1`): The starting line number (starts at 1 instead of 0).
#
# 3. WHY `len(line)` VS `line_no`?
#    - `line` is a string containing the text of a single line. `len(line)` gives the number of CHARACTERS in that string.
#    - `line_no` is the counter variable maintained by enumerate. It gives the total NUMBER OF LINES!

    