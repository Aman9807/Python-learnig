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
    goals.append(input())

# Open file in Write mode ('w') using context manager 'with'
with open(sample_file, 'w') as file:
    file.write(f"Goal 1 : {goals[0]}\n")
    file.write(f"Goal 2 : {goals[1]}\n")
    file.write(f"Goal 3 : {goals[2]}\n")

print("Goals written successfully in the file")
