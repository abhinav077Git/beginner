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
computer_parts = []  # creating empty list
while available_choice != "0":
    if available_choice in available_parts:
        current_part = available_parts[available_choice]
        # adding if items is already there
        if current_part in computer_parts:
            print(f"removing {current_part} from list")
            computer_parts.remove(current_part)
        else:
            print(f"adding {current_part} into the list")
            computer_parts.append(current_part)
        print(f"your list now contains {computer_parts}")
    else:
        print("Please choose an option from below list:")
        for key, value in available_parts.items():
            print(f"{key}:{value}")
        print("0: To Finish")

    available_choice = input("> ")
print(computer_parts)
