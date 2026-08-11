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