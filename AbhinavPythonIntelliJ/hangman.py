import random
from hangman_art import logo, stages
from hangman_words import word_list

print(logo)
random_word = random.choice(word_list)
print(random_word)
display = []
lives = 6
for word in random_word:
    display.append("_")
# print(display)
game_end = False
while not game_end:
    guess = input("Guess letter \n").lower()
    if guess in display:
        print(f"you already guessed word,{guess}")

    # for letter in random_word:
    #   if guess == letter:
    #     print("right")
    #   else:
    #     print("wrong")
    # random_word=list(random_word)
    for i in range(len(random_word)):
        if guess == random_word[i]:
            display[i] = guess

    if guess not in random_word:
        print(f"you guessed {guess} , which is not in list and lose life")
        lives = lives - 1
        if lives == 0:
            game_end = True
            print("you lose")
    # pria
    print(f"{' '.join(display)}")
    # print(display)

    if "_" not in display:
        game_end = True
        print("you win")
    print(stages[lives])

# print(random_word)
