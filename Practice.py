# name = input("What is your name?")
# print("Your name is: ", name)

# print(input("Name: "))

# age = int(input("Age"))
# print(age)

# hight = float(input("Hight: "))
# print(hight)
# print(type(hight))

# name = str(input("Name is : "))
# print(name)
# # print(type(name))

# name = input("Name: ")
# age = int (input("Age: "))
# hight = float(input("Hight: "))
# rollNO = str(input("Roll NO: "))
# # print(name, age, hight, rollNO)

# # roll = input("Roll No: ")
# # print(roll)

# print("Name:", name, "Age:", age, "Hight", hight, "rollNO:", rollNO)

# age = int(input("What is your age: "))

# if(age < 18 and age > 0):
#     print("You can not Vote.")
# elif(age >= 18 and age <100):
#     print("You can vote.")
# else:
#     print("Are you a human")
#     print("You have puted wrong")


# light = input("Colour of Light: ")

# if(light == "Red" or light == "red"):
#     print("STOP the vehicale.")
# elif(light == "Yellow" or light == "yellow"):
#     print("Start and ready.")
# elif(light == "Green" or light == "green"):
#     print("Go now.")
# else:
#     print("Light is broken.")

# mark = int(input("How much you score: "))

# if(mark >= 90 and mark <= 100):
#     print("Grade: A+")
# elif(mark >= 80 and mark < 90):
#     print("Grade: A")
# elif(mark >= 70 and mark < 80):
#     print("Grade: B+")
# elif(mark >= 60 and mark <70):
#     print("Grade: B")
# else:
#     print("You are not in first division.")

credit = float(input("Your Credit Score: "))
if(credit >= 0 and credit < 5):
    print("You have bad credit score.")
    print("You are not elligible for loan.")
elif(credit >= 5 and credit <7):
    print("You should apply loan and wait.")
elif(credit >= 7 and credit <= 10):
    print("You are elligible.")
else:
    print("You have entered wrong.\n You can try once more.")