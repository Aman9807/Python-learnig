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
