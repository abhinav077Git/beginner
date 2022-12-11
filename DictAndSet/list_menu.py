available_parts = ["computer", "mouse", "keyboard", "cpu", "monitor", "hdmi cable", "dvd drive"]
valid_choice = []  # valid choices of list from available part
for i in range(1, len(available_parts) + 1):
    valid_choice.append(str(i))
print(valid_choice)