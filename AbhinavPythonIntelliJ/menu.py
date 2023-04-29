# ####1st version#####
# def options():
#     print("Please choose option from below:")
#     print("1:\tLearn Python")
#     print("2:\tPlay Cricket ")
#     print("3:\tGot Office work")
#     print("4:\tPlay Video Games")
#     print("0:\tExit")
# option_chosen=True
# choice="-"
# while option_chosen:
#     if choice == "0":
#         break
#     elif choice in "1234":
#         print(f"you chose {choice}")
#     else:
#         options()
#     choice=input()

####2nd version####
# def options():
#     print("Please choose option from below:")
#     print("1:\tLearn Python")
#     print("2:\tPlay Cricket ")
#     print("3:\tGot Office work")
#     print("4:\tPlay Video Games")
#     print("0:\tExit")
# choice="-"
# while choice!=0:
#     if choice in "1234":
#         print(f"you chose {choice}")
#     else:
#         options()
#     choice=input()


####3rd version####

# option_chosen=True
# choice="-"
# while option_chosen:
#     if choice == "0":
#         break
#     elif choice in "1234":
#         print(f"you chose {choice}")
#     else:
#         print("Please choose option from below:")
#         print("1:\tLearn Python")
#         print("2:\tPlay Cricket ")
#         print("3:\tGot Office work")
#         print("4:\tPlay Video Games")
#         print("0:\tExit")
#     choice=input()

choice = "-"
choice_list=[]
while choice!="0":
    if choice in "123456":
        print(f"you chose {choice} and added to list")
        if choice == "1":
            choice_list.append("computer")
        elif choice == "2":
            choice_list.append("mouse")
        elif choice == "3":
            choice_list.append("keyboard")
        elif choice == "4":
            choice_list.append("cpu")
        elif choice == "5":
            choice_list.append("monitor")
        elif choice == "6":
            choice_list.append("hdmi cable")
    else:
        print("choose an option from below:")
        print("1:\tcomputer")
        print("2:\tmouse")
        print("3:\tkeyboard")
        print("4:\tcpu")
        print("5:\tmonitor")
        print("6:\thdmi cable")
        print("0:\tfinish")
    choice=input()
print(choice_list)