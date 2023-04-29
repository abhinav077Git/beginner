# numbers="9,223;372:036 854,775;807"
# seperators=""

# for char in numbers:
#     if not char.isnumeric():
#         seperators=seperators+char
# print(seperators)

# quote = """
# Alright, but apart from the Sanitation, the Medicine, Education, Wine,
# Public Order, Irrigation, Roads, the Fresh-Water System,
# and Public Health, what have the Romans ever done for us?
# """
# capital=""
# for char in quote:
#     if char.isupper():
#         capital=capital+char
# print(capital)

# shopping_list=["Abhinav","Ankit","Vaishali","Beeru","Sachin","Ritu"]
# item_to_find="Anokhe"
# found_at_position=None
# for index in range(len(shopping_list)):
#     if shopping_list[index]==item_to_find:
#         found_at_postion=index
#         break

# if found_at_position is not None:
#     print(f"{item_to_find} found at {found_at_position}")
# else:
#     print(f"{item_to_find} not found")


# for i in range(0, 100, 7):
#     print(i)
#     if i > 0 and i % 11 == 0:
#         break
#     # print(i)

# for i in range (1,21):
#     if i % 3==0 or i % 5==0:
#         continue
#     print(i)

# for i in range (1,21):
#     if i % 3!= 0 and i % 5!= 0:
#         print(i)
# str="Abhinav"
# print(str.capitalize())

# for x in range(30):
#     if x % 3 == 0 or x % 5 == 0:
#         continue
#     print(x)

# for x in range(30):
#     if x % 3 != 0 and x % 5 != 0:
#         print(x)

# quote = """
# It's not pining. It's passed on. This parrot is no more. It has ceased to be.
# It's expired and gone to meet its maker.
# This is a late parrot.
# It's a stiff. Bereft of life, it rests in peace.
# If you hadn't nailed it to the perch, it would be pushing up the daisies.
# It's rung down the curtain and joined the choir invisible.
# THIS IS AN EX-PARROT.
# """
 
# period_count = 0
# for char in quote:
#     if char == '.':
#         period_count = period_count + 1
# print(period_count)

# choice = None
 
# while choice != '0':
#     choice = input("Please enter your choice.  Press enter to quit")
#     if choice == '':
#         break
 
#     print("You have selected {}".format(choice))
# else:
#     print("Thank you for playing, please call back soon.")

# available_exit=["east","west","north","south"]
# chosen_exit=""

# while chosen_exit not in available_exit:
#     chosen_exit=input("Enter direction to exit: ")
#     if chosen_exit.casefold() == "quit":
#         print("Game Over")
#         break
# else:
#     print("Happy to get out of there")

