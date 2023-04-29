import random


def get_integer(prompt):
    """_summary_

    Args:
        prompt (_type_): _description_

    Returns:
        _type_: _description_
    """
    while True:
        temp = input(prompt)
        if temp.isnumeric():  # check whether number inputted is interger or not
            return int(temp)
        # else:
        #     print(f"Not a valid number: {temp}")
        print(f"Not a valid number: {temp}")


highest_num = 100
answer = random.randint(1, highest_num)
print(answer)
guess = 0  # to any number that does not equal to 0
print(f"Guess number between 1 and {highest_num}: ")
while guess != answer:
    # guess=int(input("Guess number between 1 and {highest_num}: "))
    guess = get_integer(": ")
    if guess == 0:
        break
    elif guess == answer:
        print("well done!! you guessed it correctly")
        break
    elif guess < answer:
        print("Please guess higher number: ")
    else:
        print("Please guess lower number: ")
