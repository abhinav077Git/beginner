# parrot = "Norwegian Blue"
# # print(len(parrot))
#
# a = parrot[3] + parrot[4] + ' ' + parrot[3] + parrot[6] + parrot[8]
# # print(a)
#
# # for i in a:
# #     print(i)
# # print(parrot[3])
# # print(parrot[4])
# # print()
# # print(parrot[3])
# # print(parrot[6])
# # print(parrot[8])
# # reverse indexing
# # print(parrot[-11])
# # print(parrot[-10])
# # print()
# # print(parrot[-11])
# # print(parrot[-8])
# # print(parrot[-6])
#
# # index slicing
# # print(parrot[0:6])
# # print(parrot[0:9])
# # print(parrot[:9])
# # print(parrot[10:14])
# # print(parrot[10:])
# # print(parrot[6:])
# # print(parrot[:6])
# # print(parrot[:6]+parrot[6:])
# # print(parrot[:])
#
# # index slicing with negative
# # print(parrot[0:6])
# # print(parrot[-14:-8])
# # print(parrot[-4:-2])
# # print(parrot[-4:12])
#
# # slicing with step
# print(parrot)
# print(parrot[1:6:2])
# print(parrot[0:6:3])
#
# number = "9,223,372,036,854,775,807"
# numbers = "9,223;372:036 854,775;807"
# seperators = numbers[1::4]
# print(seperators)
# print(number[1::4])
#
# # slicing backwards
# letters = "abcdefghijklmnopqrstuvwxyz"
# print(len(letters))
# # backwards = letters[25::-1]
# backwards = letters[::-1]  # reversing string
# print(backwards)
# print(letters.index("q"))
# print(letters.index("p"))
# # print(letters.index("o"))
# # print(letters[16:13:-1])
# # print(letters[-1:-9:-1])
# print(letters)
# # print(letters[-4:2:-1])
# # print(letters[4:-5:1])
# print(letters[25:17:-1])
# print(letters[4::-1])
# print(letters[-5:4:-1])
# print(letters[4::-1])
# # print(letters[-4])
# # print(letters[-1])
# # print(letters[:1])


# looping statement

# unit = int(input("Enter number:"))
#
# if unit < 100:
#     print(f"No charge")
# elif 100 < unit <= 200:
#     print(f"bill is {(unit - 100)*5}")
# else:
#     print(f"bill is {(unit - 200)*10 + 500}")


# guessing game

answer = 5

# print("Guess number:")
# guess = int(input())

# if guess != answer:
#     if guess < answer:
#         print("Please guess higher")
#     else:
#         print("Please guess lower")
#     guess = int(input())
#     if guess == answer:
#         print("well done! you guessed it")
#     else:
#         print("not guessed correctly")
# else:
#     print("well done!! you guessed correctly first time")
#####################################################################
# if guess == answer:
#     print("well done!! you guessed correctly first time")
# else:
#     if guess < answer:
#         print("Please guess higher")
#     else:
#         print("Please guess lower")
#     guess = int(input())
#     if guess == answer:
#         print("well done! you guessed it")
#     else:
#         print("not guessed correctly")
#####################################################################

# number = "9,223;372:036 854,775;807"
# seperator = ""
# for char in number:
#     if not char.isnumeric():
#         seperator = seperator + char
#
# print(seperator)

# quote = """
# Alright, but apart from the Sanitation, the Medicine, Education, Wine,
# Public Order, Irrigation, Roads, the Fresh-Water System,
# and Public Health, what have the Romans ever done for us?
# """
#
# # Use a for loop and an if statement to print just the capitals in the quote above.
# for char in quote:
#     if char.isupper():
#         print(char)

# shopping_list = ["milk", "eggs", "bread", "spam", "pasta", "rice"]

# for item in shopping_list:
# if item != "spam":
#     print(f"Buy " + item)
##########################################
# if item == "spam":
#     continue
# print(f"Buy {item}")
##############################################
# if item == "spam":
#     break
# print(f"Buy {item}")

# searching item through list
shopping_list = ["milk", "eggs", "bread", "spam", "pasta", "rice"]

item_to_find = "albatross"
found_at = None

# for index in range(len(shopping_list)):
#     if shopping_list[index] == item_to_find:
#         found_at = index
#         break
# print(found_at)

######################################################
# if item_to_find in shopping_list:
#     found_at = shopping_list.index(item_to_find)
# if found_at is not None:
#     print(f"found {item_to_find} at position {found_at}")
# else:
#     print(f"{item_to_find} not found")

#####################while loop##############################

# available_exit = ["east", "west", "north", "south"]
# chosen_exit = ""
# while chosen_exit not in available_exit:
#     chosen_exit = input("Please choose the direction: ")
#     if chosen_exit.casefold() == "quit":
#         print("Game Over")
#         break
#
# print("Glad you got out of there")

# for i in range(0, 100, 7):
#     print(i)
#     if i > 0 and i % 11 == 0:
#         break
# printing the string seperated by comma
numbers = "9,223;372:036 854,775;807"
seperators = numbers[1::4]
print(seperators)

for char in numbers:
    if char in seperators:
        numbers = numbers.replace(char, ",")
print(numbers)
