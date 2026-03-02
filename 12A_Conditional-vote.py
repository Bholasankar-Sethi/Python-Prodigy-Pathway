age = int(input("What is your Age? "))

if(age >= 18):
  print("You can vote.")
  print("You are an adult.")
elif(age < 18):
  print("You cannt vote", "You are Young", "Not adult.")
else:
  print("You are wrong.")