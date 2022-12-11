available_parts = {
    "1": "computer",
    "2": "mouse",
    "3": "keyboard",
    "4": "cpu",
    "5": "monitor",
    "6": "hdmi cable",
    "7": "dvd drive"
}

# print("mouse" in available_parts)  # return False as 'in' keyword in dictionary  checks for key not value
# print("4" in available_parts)  # return True as 'in' keyword in dictionary check for key not value

# available_parts = ["computer", "mouse", "keyboard", "cpu", "monitor", "hdmi cable", "dvd drive"]
#
# print("mouse" in available_parts)  # return True as 'in' keyword in List checks for items
# print("4" in available_parts)  # return True as 'in' keyword in List checks for items

available_choice = None
computer_choice = {}  # creating empty dictionary
while available_choice != "0":
    if available_choice in available_parts:
        current_part = available_parts[available_choice]  # items given(in list) but here it is value of key
        if available_choice in computer_choice:
            print(f"removing {current_part}")
            computer_choice.pop(available_choice)  # pop the key from the dictionary
        else:
            print(f"Adding {current_part}")
            computer_choice[available_choice] = current_part  # assigning the key with value in dictionary
        print(f"Your dictionary now contains: {computer_choice}")
    else:
        print("Please choose an option from below list:")
        for key, value in available_parts.items():
            print(f"{key}:{value}")
        print("0: To Finish")

    available_choice = input("> ")

print(computer_choice)
