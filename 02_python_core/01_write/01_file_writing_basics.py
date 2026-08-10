# Topic: File Handling - Writing Files (Month 2: Core Python)
#
# Key Concepts:
# 1. Opening a file: `open(filename, mode)`
#    Modes:
#    - 'w' : Write mode (creates a new file or OVERWRITES existing content)
#    - 'a' : Append mode (adds content to the end of an existing file)
#    - 'r' : Read mode (default)
# 2. Context Manager (`with open(...) as file:`):
#    - Automatically closes the file when done, even if errors occur!
#    - ALWAYS recommended over manual `open()` and `close()`.
# 3. Writing methods:
#    - `file.write("text\n")` : Writes a string to the file (add '\n' for newlines).
#    - `file.writelines(list)` : Writes a list of strings to the file.

# ----------------------------------------------------
# Demonstration Code:
# ----------------------------------------------------
# import os

# # Create notes directory if needed
# os.makedirs("02_python_core", exist_ok=True)

# sample_file = "02_python_core/sample_notes.txt"

# print("--- Writing Sample File ---")
# with open(sample_file, "w") as file:
#     file.write("Welcome to Month 2: Core Python!\n")
#     file.write("Today we are learning File Handling.\n")
#     file.write("Files allow us to save data permanently on disk.\n")

# print(f"Saved demo notes to: {sample_file}\n")


# ====================================================
# YOUR PRACTICE TASK:
# ====================================================
# Problem Statement:
# Create a program that prompts the user to enter 3 learning goals for Month 2.
# Save those goals into a file named `02_python_core/my_goals.txt`.
#
# Steps to complete:
# 1. Ask the user for 3 goals using input().
# 2. Open `02_python_core/my_goals.txt` in write mode ('w') using `with open(...)`.
# 3. Write each goal formatted as:
#    Goal 1: <user goal 1>
#    Goal 2: <user goal 2>
#    Goal 3: <user goal 3>
# 4. Print a success message confirming the file was created!
#
# Write your solution code below:

# Import the 'os' module to interact with your operating system (folders & files)
import os

# Create folder '02_python_core/01_write' if it doesn't exist yet
os.makedirs("02_python_core/01_write", exist_ok=True)

# Define the relative path of the file we want to write to
sample_file = "02_python_core/01_write/write_goals.txt"

print("----Writing your goals----")

# Initialize an empty list to store user goals
goals = []

# Loop 3 times to get 3 goals from the user
for i in range(3):
    print(f"Enter your goal number {i+1}: ")
    # Use .append() to add each input string to the end of the empty list
    goals.append(input())

# Open file in Write mode ('w') using context manager 'with' (automatically closes file when done)
with open(sample_file, 'w') as file:
    file.write(f"Goal 1 : {goals[0]}\n")
    file.write(f"Goal 2 : {goals[1]}\n")
    file.write(f"Goal 3 : {goals[2]}\n")

print("Goals written successfully in the file")


# ====================================================
# SUMMARY NOTES FOR REVISION:
# ====================================================
# 1. WHAT IS `import os` AND `os.makedirs()`?
#    - `os` stands for Operating System. It allows Python to talk to your OS (Windows/Mac/Linux).
#    - `os.makedirs("folder_name", exist_ok=True)` creates a new folder.
#    - `exist_ok=True` prevents Python from crashing if the folder already exists.
#
# 2. WHAT IS `with open(sample_file, 'w') as file:`?
#    - `with`: Context Manager. Automatically closes the file safely when finished (even if code crashes!).
#    - `'w'`: Write mode. Creates a new file or overwrites existing file content.
#    - `as`: Assigns the opened file object to a variable name.
#    - `file`: Variable name representing the opened file. You can change `file` to any valid variable name:
#        with open(sample_file, 'w') as f:
#        with open(sample_file, 'w') as my_file:
#
# 3. WHY USE `goals.append(input())` INSTEAD OF `goals[i] = input()`?
#    - An empty list `goals = []` has length 0 (no positions 0, 1, or 2 exist yet).
#    - `goals[0] = ...` will crash with `IndexError: list assignment index out of range`.
#    - `.append()` grows the list dynamically by pushing items to the end!




    



