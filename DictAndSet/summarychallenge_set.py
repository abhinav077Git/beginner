choice = "-"  # initialise choice to something invalid   

while choice != "0":
    # if choice in "12345":
    # if choice in set("12345"): #{"1","2","3","4","5"}
    if choice in list("12345"):  # ["1","2","3","4","5"]
        print(f"you chose {choice}")
    else:
        print("Please choose an option from below: ")
        print("1:\tLearn Python")
        print("2\tLearn Java")
        print("3\tGo Swimming")
        print("4\tHave Dinner")
        print("5:\tGo to Bed")
        print("0:\tExit")

    choice = input()
