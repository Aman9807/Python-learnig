# A program to practice dictionary looping in Python to store subject marks for a student.
marks = {}
for i in range(1, 4):
    subject = input(f"Enter subject {i} name: ")
    mark = float(input(f"Enter marks for {subject}: "))
    marks[subject] = mark

for subject, mark in marks.items():
    print(f"{subject}: {mark}")

total = sum(marks.values())
average = total / len(marks)

print(f"Total Marks: {total}")
print(f"Average Marks: {average:.2f}")

print(f"All Subject and Marks: {marks}")

