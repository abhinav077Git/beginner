####finding random number####
# import random
# random_integer=random.randint(1,10)
# print(random_integer)

# random_float=random.random() * 5
# print(random_float)

# love_score=random.randint(1,100)
# print(f"Your score is {love_score}")
# ####Head or tail######
# import random
# random_number=random.randint(0,1)
# if random_number == 0:
#   print("Heads")
# else:
#   print("Tails")

####random pick from list of name who will buy and pay the bill #####
# import random

# # 🚨 Don't change the code below 👇
# test_seed = int(input("Create a seed number: "))
# random.seed(test_seed)

####Rock,paper,scissors###
import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
options=[rock,paper,scissors]
#Write your code below this line 👇
user_choice=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
computer_choice=random.randint(0,2)
# print(f"You choose:{user_choice}")
print(f"{options[user_choice]}");
# print(f"computer choose: {computer_choice}")
print(f"{options[computer_choice]}");
if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number.. You lose!!")
elif user_choice ==1 and computer_choice == 0:
    print ("You wins!!")
elif computer_choice == 0 and user_choice == 2:
    print("You lose!!")
elif user_choice == 0 and computer_choice ==2:
    print("You wins!!")
elif computer_choice > user_choice:
    print("You lose!!")
elif user_choice > computer_choice:
    print ("You wins!!")
else:
    print("It is draw!!")
  

