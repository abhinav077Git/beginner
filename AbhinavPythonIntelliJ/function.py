# def myFunction():
#   print("Hello")
#   print("Abhinav")
# myFunction()

# def addTwo(num1,num2):
#   return num1 + num2
# print(addTwo(5,3))

def findNum(array, target):
    for num in range(len(array)):
        if target == array[num]:
            return num
    return -1


find = findNum([1, 2, 3, 4], 2)
print(find)

# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
# def turn_right1():
#     turn_left()
#     turn_left()
# def MOVE():
#     move()
# #square
# turn_left()
# MOVE()
# turn_right()
# MOVE()
# turn_left()
# turn_right1()
# MOVE()
# turn_right()
# MOVE()
# turn_left()
# turn_left()

# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()

# def jump():
#   move()
#   turn_left()
#   move()
#   turn_right()
#   move()
#   turn_right()
#   move()
#   turn_left()

# num_of_hurdles=6
# while num_of_hurdles > 0:
#     jump()
#     num_of_hurdles=num_of_hurdles-1


# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()

# def jump():
#   turn_left()
#   move()
#   turn_right()
#   move()
#   turn_right()
#   move()
#   turn_left()    
# while not at_goal():
#     if wall_in_front():
#         jump()
#     elif front_is_clear():
#         if not at_goal():
#             move()
#         elif wall_in_front():
#             jump()
#         else:
#             at_goal()
#     else:
#         move()
