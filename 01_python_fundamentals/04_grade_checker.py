name = input("Enter your name\n")
marks = int(input("Enter your marks\n"))
if(marks<=100 and marks>=0):

    if (marks>=90):
        print("A Grade")
    elif(marks>=75):
      print("B Grade")
    elif(marks>=40):
      print("C Grade")
    else:
      print("Failed")

else:
   print("Enter Correct marks")
   