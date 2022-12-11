# import random
#
# highest = 10
# answer = random.randint(1, highest)
# print(answer)

# print(f"Guess number between 1 and {highest}: ")
# guess = int(input())
######################using if else###############################
# if guess == answer:
#     print("Well done!! you guessed it first time")
# else:
#     if guess < answer:
#         print("Please guess higher")
#     else:
#         print("Please guess lower")
#     guess = int(input())
#     if guess == answer:
#         print("You guessed it correctly")
#     else:
#         print("Sorry wrong guess")

###########################using while########################################
# guess = 0
# while guess != answer:
#     guess = int(input())
#     if guess == answer:
#         print("well done!! you guessed correctly")
#         break
#     else:
#         if guess < answer:
#             print("Please guess higher")
#         else:
#             print("Please guess lower")

#################################################################

# binary chop
# low = 1
# high = 100
#
# print(f"guess number between {low} and {high}")
#
# guesses = 1
# while True:
#     print(f"Guess in the range of {low} and {high}")
#     guess = low + (high - low) // 2
#     high_low = input(f"My guess is {guess}...Guess if number is higher,lower or correct!! Type 'h' for higher,'l' for "
#                      f"lower and 'c' for "
#                      "correct: ").casefold()
#     if high_low == "h":
#         # low end of range value becomes 1 greater than guess
#         low = guess + 1
#     elif high_low == "l":
#         # high end of range become 1 less than guess
#         high = guess - 1
#     elif high_low == "c":
#         print(f"guess correctly in {guesses}")
#         break
#     else:
#         print("Please type 'h','l' or 'c': ")
#     guesses = guesses + 1

#######################################################################
# low = 1
# high = 1000
#
# print(f"guess number between {low} and {high}")
#
# guesses = 1
# while low != high:
#     # print(f"Guess in the range of {low} and {high}")
#     guess = low + (high - low) // 2
#     high_low = input(f"My guess is {guess}...Guess if number is higher,lower or correct!! Type 'h' for higher,'l' for "
#                      f"lower and 'c' for "
#                      "correct: ").casefold()
#     if high_low == "h":
#         # low end of range value becomes 1 greater than guess
#         low = guess + 1
#     elif high_low == "l":
#         # high end of range become 1 less than guess
#         high = guess - 1
#     elif high_low == "c":
#         print(f"guess correctly in {guesses}")
#         break
#     else:
#         print("Please type 'h','l' or 'c': ")
#     guesses = guesses + 1
#
# else:
#     print(f"You got you correct {low} in {guesses} times")
# number = 5
# multiplier = 8
# answer = 0
#
# # add your loop after this comment
# for index in range(1, multiplier + 1):
#     answer = answer + number
#
# print(answer)

options_to_choose="-"
while True:
    if options_to_choose == "0":
        print(f"you have chosen option: {options_to_choose} so Exit")
        break
    elif options_to_choose in "12345":
        print(f"You have chosen an options {options_to_choose}")
    else:
        print("Please choose an option from below: ")
        print("1. Learn Python")
        print("2. Learn Java")
        print("3. Go Swimming")
        print("4. Have Dinner")
        print("5. Go to Bed")
        print("0. Exit")
    options_to_choose = input()
