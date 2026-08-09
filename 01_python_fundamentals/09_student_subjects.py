sub = ["Python", "Maths", "English", "Science"]
print(sub)
print(sub[0])       # First item: Python
print(sub[-1])      # Last item: Science
sub.append(input("Enter a new subject: "))  # Adding a new subject to the list
print(f"{sub}, which subject you want to replace?")
sub[int(input("Enter the index of the subject you want to replace: "))] = input("Enter the new subject: ")  # Replacing a subject at a specific index
print(sub)
print(f"Total number of subjects: {len(sub)}")  # Printing the total number of subjects 