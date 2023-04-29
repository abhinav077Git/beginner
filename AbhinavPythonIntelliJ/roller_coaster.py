print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
if height > 120:
  print("you can ride")
  age=int(input("what is your age ? \n"))
  if age < 12:
    print("please pay 5$")
  else:
    print("please pay 7$")
else:
  print("you cant ride.")

#################################################3

# calculating ticket according to height and age
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
if height > 120:
  print("you can ride")
  age=int(input("what is your age ? \n"))
  if age < 12:
    print("please pay 5$")
  elif age <= 18:
      print("please pay 7$")
  else:
    print("please pay 12$")
else:
  print("you cant ride.")