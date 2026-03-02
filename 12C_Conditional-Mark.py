mark = int(input("Mark: "))

if(mark >= 90 and mark <= 100):
  print("Grade: A+")
elif(mark >= 80 and mark < 90):
  print("Grade: A")
elif(mark >= 70 and mark < 80):
  print("Grade: B+")
elif(mark >= 60 and mark < 70):
  print("Grade: B")
elif(mark < 0 or mark > 100):
  print("Wrong input.")
else:
  print("Not First Division.")