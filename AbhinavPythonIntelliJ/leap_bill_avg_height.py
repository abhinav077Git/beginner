###################################################
#finding given year is leap year

# 🚨 Don't change the code below 👇
# year = int(input("Which year do you want to check? "))
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇
# if year % 4 == 0:
#   if year % 100 == 0:
#     if year % 400 ==0:
#       print("Leap year.")
#     else:
#       print ("Not leap year")
#   else:
#     print("Leap Year.")
# else:
#   print("Not leap year.")

###################################################
#calculating totol bill according to height ,age and whoever wants photos
# height=int(input("Enter your height in cm: \n"))
# bill=0
# if height > 120:
#     print("You can ride.")
#     age=int(input("enter your age: \n"))
#     if age < 12:
#         bill=5
#         print("child ticket is $5")
#     elif age <=18:
#         bill=7
#         print("youth ticket is $7")
#     elif age >=45 and age <=55:
#       print("Everything is going to be OK, ticket is free,Enjoy!!")
#     else:
#         bill=12
#         print("adult ticket is $12")
#     want_photos=input("Do you want photos!! Y or N \n")
#     if want_photos == "Y":
#         bill= bill+3
#     print(f"Your bill is {bill}")
# else:
#     print("You cant ride")
# ####################################################
# #calculating pizza bill according to size,want pepporini or cheese
# # 🚨 Don't change the code below 👇
# print("Welcome to Python Pizza Deliveries!")
# size = input("What size pizza do you want? S, M, or L ")
# add_pepperoni = input("Do you want pepperoni? Y or N ")
# extra_cheese = input("Do you want extra cheese? Y or N ")
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇
# bill=0
# if size == "S":
#     bill=15
#     if add_pepperoni == "Y":
#         bill= bill + 2
#     if extra_cheese == "Y":
#         bill= bill + 1
#     print(f"Your final bill is: ${bill}.")
# elif size == "M":
#     bill=20
#     if add_pepperoni == "Y":
#         bill= bill + 3
#     if extra_cheese == "Y":
#         bill= bill + 1
#     print(f"Your final bill is: ${bill}.")
# elif size == "L":
#     bill=25
#     if add_pepperoni == "Y":
#         bill= bill + 3
#     if extra_cheese == "Y":
#         bill= bill + 1
#     print(f"Your final bill is: ${bill}.")
# else:
#     print(f"Your final bill is: ${bill}.")

#####calculating average height of students####
# # 🚨 Don't change the code below 👇
# student_heights = input("Input a list of student heights ").split()
# for n in range(0, len(student_heights)):
#   student_heights[n] = int(student_heights[n])
# # 🚨 Don't change the code above 👆


# #Write your code below this row 👇
# # print(student_heights)
# total=0
# i=0
# for height in student_heights:
#   total=total+height
#   i=i+1
# # print(total)
# # print(i)
# average = round(total / i)
# print(average)
