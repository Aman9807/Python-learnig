# Topic: File Handling - Append Mode & Mini Journal App (Month 2: Core Python)
#
# Key Concepts:
# 1. Append Mode (`'a'`):
#    - Opens a file for writing, but PRESERVES existing content and adds new text to the END.
#    - Creates the file if it does not already exist.
# 2. `datetime` module:
#    - `datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")` generates a readable date & time string.
# 3. `if __name__ == "__main__":`
#    - Ensures `main()` runs ONLY when the script is executed directly.

# ----------------------------------------------------
# Demonstration Code (Commented Out for Reference):
# ----------------------------------------------------
# import datetime
# import os
#
# journal_file = "02_python_core/daily_journal.txt"
#
# def add_entry():
#     entry = input("Enter your note: ")
#     timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#     with open(journal_file, "a") as file:
#         file.write(f"[{timestamp}] {entry}\n")
#     print("Entry saved successfully!\n")
#
# def view_entries():
#     if not os.path.exists(journal_file):
#         print("No journal file found yet!\n")
#         return
#     with open(journal_file, "r") as file:
#         for line in file:
#             print(line.strip())
#
#         print("--- MINI JOURNAL APP ---")
#         print("1. Add Note")
#         print("2. View Notes")
#         print("3. Exit")
#         choice = input("Choose option (1-3): ")
#         
#         if choice == "1":
#             add_entry()      # Calls the add_entry() function above
#         elif choice == "2":
#             view_entries()   # Calls the view_entries() function above
#         elif choice == "3":
#             print("Goodbye!")
#             break            # Exit the loop
#         else:
#             print("Invalid choice, try again!\n")
#
# # Call the main function to start the app:
# if __name__ == "__main__":
#     main()


# ====================================================
# SUMMARY NOTES FOR REVISION:
# ====================================================
# 1. WHAT IS APPEND MODE (`'a'`)?
#    - Mode `'w'` overwrites/deletes existing file content.
#    - Mode `'a'` appends new text at the end without deleting anything!
#
# 2. HOW DOES `datetime` WORK?
#    - `import datetime` fetches current time.
#    - `now = datetime.datetime.now()` gets the raw current date & time.
#    - `now.strftime("%Y-%m-%d %H:%M:%S")` formats time into "YYYY-MM-DD HH:MM:SS".
#        %Y = 4-digit year, %m = month, %d = day
#        %H = 24-hr hour, %M = minute, %S = second
#
# 3. WHAT IS `if __name__ == "__main__":`?
#    - `__name__` is a built-in variable in Python.
#    - When running file directly in terminal, `__name__` equals `"__main__"`.
#    - Ensures main menu runs only when executing this file directly (not when imported).


# ====================================================
# YOUR PRACTICE TASK:
# ====================================================
# Problem Statement:
# Build a Daily Task Logger program that appends new tasks with timestamps
# to a file named `02_python_core/daily_log.txt`.
#
# Steps to complete:
# 1. Import `datetime` and `os`.
# 2. Create a function `add_log()`:
#    - Prompt user for a task description.
#    - Get current timestamp using `datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")`.
#    - Open `02_python_core/daily_log.txt` in append mode ('a').
#    - Write: `[{timestamp}] Task: {description}\n`
#    - Print a success confirmation message.
#
# 3. Create a function `view_logs()`:
#    - Check if `02_python_core/daily_log.txt` exists using `os.path.exists()`.
#    - Open `02_python_core/daily_log.txt` in read mode ('r').
#    - Loop through each line and print it out cleaned with `.strip()`.
#
# 4. Create a `main()` function with a `while True:` loop menu:
#    1. Add Task Log
#    2. View All Logs
#    3. Exit
#
# 5. Add the execution check at the bottom:
#    `if __name__ == "__main__": main()`
#
# Write your solution code below:
# Import required modules: datetime for timestamps, os for file system checks
import datetime
import os

# Define the log file path
journal_file = "02_python_core/03_append/daily_log.txt"

# Function to prompt user and append a new log entry
def add_log():
    task = input("Enter your task: ")
    # Format current date and time
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # Open in append mode ('a') so existing entries aren't lost
    with open(journal_file, 'a') as file:
        file.write(f"[{timestamp}] Task: {task}\n")
        print(f"Entry added successfully to {journal_file}\n")

# Function to read and display all logged entries
def read_log():
    if not os.path.exists(journal_file):
        print("No journal file found yet!\n")
        return

    with open(journal_file, "r") as file:
        for line in file:
            print(line.strip())
        print()

# Main menu loop function
def main():
    while True:
        print("--- MINI JOURNAL APP ---")
        print("1. Add Note")
        print("2. View Notes")
        print("3. Exit")
        choice = input("Choose option (1-3): ")
        if choice == "1":
            add_log()
        elif choice == "2":
            read_log()
        elif choice == "3":
            print("Goodbye! Exiting application.\n")
            break
        else:
            print("Invalid choice, try again!\n") 

# Execution entry point
if __name__ == "__main__":
    main()

