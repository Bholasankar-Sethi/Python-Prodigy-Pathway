#A = int(input("A = "))
#G = input("G = ")

# Input - 1
A, G = 5, "M"

if((A == 1 or A == 2) and G == "M"):
  print("Fee is 100.")
elif(A == 3 or A == 4 or G == "F"):
  print("Fee is 200.")
elif(A == 5 and G == "M"):
  print("Fee is 300.")
else:
  print("No Fee.")


# Input - 2

A, G = 2, "F"

if((A == 1 or A == 2) and G == "M"):
  print("Fee is 100.")
elif(A == 3 or A == 4 or G == "F"):
  print("Fee is 200.")
elif(A == 5 and G == "M"):
  print("Fee is 300.")
else:
  print("No Fee.")