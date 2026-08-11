# Topic: Exception Handling in Python (Month 2: Core Python)

# Key Concepts:
# 1. What is an Exception?
#    - An error that occurs while a program is running, causing Python to crash.
# 2. Common Built-in Exceptions:
#    - ValueError       : Triggered when a function receives an argument of right type but wrong value (e.g. `int("abc")`).
#    - ZeroDivisionError: Triggered when dividing any number by zero (e.g. `10 / 0`).
#    - FileNotFoundError: Triggered when trying to open a file that doesn't exist.
#    - KeyError         : Triggered when searching for a dictionary key that isn't present.
#    - IndexError       : Triggered when accessing a list index out of range.
#
# 3. Structure of `try-except-else-finally`:
#    try:
#        # Code that might crash
#    except SpecificError:
#        # Code that runs IF that specific error happens
#    else:
#        # Code that runs ONLY IF NO error happened
#    finally:
#        # Code that ALWAYS runs, no matter what!


# ----------------------------------------------------
# Demonstration Code (Commented Out for Reference):
# ----------------------------------------------------
# # Example 1: Safe integer input handling
# try:
#     age = int(input("Enter your age: "))
#     print(f"Next year you will be {age + 1}")
# except ValueError:
#     print("❌ Invalid input! Please enter a numeric integer.")
# else:
#     print("✅ Age recorded successfully!")
# finally:
#     print("Process finished.\n")

# # Example 2: Safe File Reading
# try:
#     with open("non_existent_file.txt", "r") as file:
#         content = file.read()
# except FileNotFoundError:
#     print("⚠️ File was not found! Check your filename.")


# ====================================================
# SUMMARY NOTES FOR REVISION:
# ====================================================
# 1. WHY USE EXCEPTION HANDLING?
#    - Prevents your program from crashing ungracefully when bad input or missing files occur.
#    - Provides clear, helpful error messages to the user.
#
# 2. `try` vs `except` vs `else` vs `finally`:
#    - `try`     : Test a block of code for errors.
#    - `except`  : Handle specific errors. (Never use bare `except:` without error types!).
#    - `else`    : Executes if the try block succeeded without any errors.
#    - `finally` : Executes always, regardless of success or errors (ideal for cleanup).


# ====================================================
# YOUR PRACTICE TASK:
# ====================================================
# Problem Statement:
# Create two safe functions to handle division and file reading without crashing!

def safe_divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("❌ Error: Cannot divide by zero!")
    except TypeError:
        print("❌ Error: Inputs must be numbers!")
    else:
        print(f"Result of {a} / {b} = {result}")

def safe_read(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
    except FileNotFoundError:
        print(f"❌ Error: The file '{file_path}' does not exist!")
    else:
        print(content.strip())

# Test calls
safe_divide(10, 2)
safe_divide(10, 0)
safe_read("02_python_core/exception_handling/test.txt")
