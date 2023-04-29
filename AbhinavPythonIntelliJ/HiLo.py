import random

low = 1
high = 1000
# answer = random.randint(1,high)
# print(answer)
# while True:
#     print("Guess a number: ")
#     guess = int(input())
#     if guess == 0:
#         break
#     elif guess == answer:
#         print("you guessed it correctly!!! well done")
#         break
#     elif guess < answer:
#         print("guess higher number")
#     else:
#         print("guess lower number")
guesses=0
while True:
    print(f"Guessing in the range {low} and {high}: ")
    guess = low + (high - low) // 2
    # print(guess)
    HiLo = input("Enter h for 'higher',l for 'lower' and c for 'correct': ")
    if HiLo.casefold() == "h":
        low = guess + 1
    elif HiLo.casefold() == "l":
        high = guess - 1
    elif HiLo.casefold() == "c":
        print(f"guess is correct and {guess} got in {guesses} guess")
        break
    else:
        print("Enter h for 'higher',l for 'lower' and c for 'correct': ")
    guesses = guesses + 1
else:
    print(f"correct number was {low} and guessed in {guesses}")
