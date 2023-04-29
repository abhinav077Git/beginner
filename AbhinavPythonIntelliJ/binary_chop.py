# answer=5
# guess=int(input("Guess number \n"))

# if guess == answer:
#     print("It is correct guess")
# else:
#     if guess < answer:
#         print("guess is lower, please guess higher number")
#     else:
#         print("guess is higher, please guess lower number")
#     guess=int(input())
#     if guess == answer:
#             print("you got it")
#     else:
#             print("wrong guess")

# if guess != answer:
#     # print("guessed not correctly, please guess correctly")
#     # guess=int(input())
#     if guess < answer:
#         print("guess higher number")
#     else:
#         print("guess lower number")
#     guess=int(input())
#     if guess == answer:
#         print("you guessed it correctly")
#     else:
#         print("wrong guessed")
# else:
#     print("you got it first time")

# import random
# highest_number=10
# answer=random.randint(1,highest_number)
# print(f"answer is {answer}")
# print("Guess number\n")
# guess_not_true=True
# while guess_not_true:
#     guess=int(input())
#     if guess == 0:
#         break
#     if guess == answer:
#         print("well done , you got the answer!!")
#         guess_not_true=False
#     else:
#         if guess < answer:
#             print("guess higher number\n")
#         else:
#             print("guess lower number\n")

###Binary chop####
# import random
# low=1
# high=1000
# input("Press ENTER to start")
# guess_true=False
# guesses=0
# while not guess_true:
#     guess=low+(high-low)//2
#     print(f"guessing in the range of {low} to {high}")
#     print(f"my guess is {guess}")
#     result=input("enter h for higher,l for lower and c if your guess is correct ")
#     if result.casefold() == "h":
#         low = guess + 1
#     elif result.casefold() == "l":
#         high = guess -1
#     elif result.casefold() == "c":
#         print("well done... you got your guessed number")
#         guess_true=True
#     else:
#         print("type h for higher,l for lower and c if correct")
#     guesses=guesses + 1
# print(f"correct answer got in {guesses} guess")


# number = 5
# multiplier = 8
# answer = 0

# # add your loop after this comment
# for index in range(1,multiplier + 1):
#     answer=answer+number

# print(answer)

low = 1
high = 1000
chance = 0
input("Press ENTER to start \n")
while low != high:
    print(f"guessing in the range {low} to {high}")
    guess = low + (high - low) // 2
    print(f"my guess is {guess}")
    result = input("Enter h for higher , l for lower or c if guess is correct: ")
    if result.casefold() == "h":
        low = guess + 1
    elif result.casefold() == "l":
        high = guess - 1
    elif result.casefold() == "c":
        print(f"You got the correct number {guess} in {chance} chances")
        break
    else:
        print(f"Enter h for higher , l for lower or c if guess is correct:")
    chance = chance + 1
else:
    print(f"correct number was {low} guessed in {chance}")
