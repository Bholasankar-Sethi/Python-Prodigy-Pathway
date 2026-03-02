light = input("Traffic light colour: ")

if(light == "Red" or light == "red"):
  print("Stop the vehicle.")
elif(light == "Yellow" or  light == "yellow"):
  print("Start and Ready.")
elif(light == "Green" or light == "green"):
  print("You can go now.")
else:
  print("Wrong Information.")