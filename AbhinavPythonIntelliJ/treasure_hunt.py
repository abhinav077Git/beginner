print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
#Write your code below this line 👇
options=input("""You're at a crossroad. Where do you want to go? Type "left" or "right" """)
if options == "left":
  options1=input("""You've" come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across. """)
  if options1 == "wait":
    options2=input("""You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?""")
    if options2 == "Red":
      print("""It's a room full of fire. Game Over.""")
    elif options2 == "Blue":
      print("""You enter a room of beasts. Game Over.""")
    elif options2 == "Yellow":
      print("""You found the treasure! You Win!""")
    else:
      print("""You chose a door that doesn't exist. Game Over.""")
  else:
    print("""You get attacked by an angry trout. Game Over.""")
else:
  print("""You fell into a hole. Game Over""")