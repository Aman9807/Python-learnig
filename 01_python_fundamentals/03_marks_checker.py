name = input("Enter your name\n")
marks  = int(input("Enter your marks\n"))
if(marks>=40):
    print(f"{name}, you passed")
else:
    print(f"{name}, you failed. You need {40 - marks} more marks to pass")