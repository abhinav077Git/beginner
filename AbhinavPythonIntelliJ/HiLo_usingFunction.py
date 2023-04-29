LOW = 1
HIGH = 1000
print(f"Please think of number between {LOW} and {HIGH}")
print("Press ENTER to start")


def guess_hilo(answer, low, high):
    guesses = 0
    while True:
        # print(f"guessing in the range {low} and {high}")
        guess = low + (high - low) // 2
        # print(guess)
        # HiLo = input("Enter h for 'higher',l for 'lower' and c for 'correct': ")
        # if HiLo.casefold() == "h":
        if guess < answer:
            low = guess + 1
        # elif HiLo.casefold() == "l":
        elif guess > answer:
            high = guess - 1
        # elif HiLo.casefold() == "c":
        elif guess == answer:
            # print(f"Guess is correct and got {guess} in {guesses} guesses")
            # break
            return guesses
        # else:
        #     print("Enter h for 'higher',l for 'lower' and c for 'correct': ")
        guesses = guesses + 1
    # else:
    #     print(f"correct number is {low} and guessed in {guesses} guesses ")


max_guesses = 0
correct_count = 0
for number in range(LOW, HIGH + 1):
    number_of_guesses = guess_hilo(number, LOW, HIGH)
    print(f"number {number} guessed in {number_of_guesses}")
    if number_of_guesses > max_guesses:
        max_guesses, correct_count = number_of_guesses, 1
    elif number_of_guesses == max_guesses:
        correct_count = correct_count + 1
print(f"I guessed without being told is {correct_count} and count is {max_guesses}")
