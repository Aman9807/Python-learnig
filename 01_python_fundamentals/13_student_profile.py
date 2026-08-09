# A program for Dictionary in Python to store student profile information.

student = {}

student["name"] = input("Enter student's name: ")
student["age"] = int(input("Enter student's age: "))
student["course"] = input("Enter student's course: ")
student["city"] = input("Enter student's city: ")

print(f"Student Profile: {student['name']}, is {student['age']} years old and is enrolled in the {student['course']} course, and lives in {student['city']}.")

student["city"] = input("Enter student's city: ")

print(f"Updated Student Profile: {student['name']}, is {student['age']} years old and is enrolled in the {student['course']} course, and lives in {student['city']}.")