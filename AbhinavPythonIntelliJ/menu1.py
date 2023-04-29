# available_parts=["computer","mouse","keyboard","cpu","monitor","hdmi cable","dvd drive"]
# choice="-"
# choice_list=[]
# while choice!="0":
#     if choice in "1234567":
#         print(f"you chose {choice} and added to list")
#         if choice == "1":
#             choice_list.append("computer")
#         elif choice == "2":
#             choice_list.append("mouse")
#         elif choice == "3":
#             choice_list.append("keyboard")
#         elif choice == "4":
#             choice_list.append("cpu")
#         elif choice == "5":
#             choice_list.append("monitor")
#         elif choice == "6":
#             choice_list.append("hdmi cable")
#         elif choice == "7":
#             choice_list.append("dvd drive")
#     else:
#         print("choose an option from below:")
#         # for part in available_parts:
#         for number,part in enumerate(available_parts):
#             # print(f"{available_parts.index(part) + 1}: {part}")
#             print(f"{number+1}:{part}")
#     choice=input()
# print(choice_list)

# enumerate function

# for index,char in enumerate("abcdefgh"):
#     print(index,char)

################################################################################3
# available list
available_parts=["computer","mouse","keyboard","cpu","monitor","hdmi cable","dvd drive"]
valid_choice=[] ## valid choices of list from available part
for i in range ( 1, len(available_parts) + 1):
    valid_choice.append(str(i))
print(valid_choice)
choice="-"
choice_list=[] ## part customer want to buy
while choice!="0":
    if choice in valid_choice:
        index = int(choice) -1
        chosen=available_parts[index]
        if chosen in choice_list:
            print(f"removing {choice} to list")
            choice_list.remove(available_parts[index])
        else:
            print(f"Adding {choice} to list")
            choice_list.append(available_parts[index])
    else:
        print("choose an option from below:")
        for part in available_parts:
        # for number,part in enumerate(available_parts):
            print(f"{available_parts.index(part) + 1}: {part}")
            # print(f"{number+1}:{part}")
    choice=input()
print(choice_list)

# data = [
#     "Andromeda - Shrub",
#     "Bellflower - Flower",
#     "China Pink - Flower",
#     "Daffodil - Flower",
#     "Evening Primrose - Flower",
#     "French Marigold - Flower",
#     "Hydrangea - Shrub",
#     "Iris - Flower",
#     "Japanese Camellia - Shrub",
#     "Lavender - Shrub",
#     "Lilac - Shrub",
#     "Magnolia - Shrub",
#     "Peony - Shrub",
#     "Queen Anne's Lace - Flower",
#     "Red Hot Poker - Flower",
#     "Snapdragon - Flower",
#     "Sunflower - Flower",
#     "Tiger Lily - Flower",
#     "Witch Hazel - Shrub",
# ]

# flowers = []
# shrubs = []

# # write your code here

# for plant in data:
#     if "Flower" in plant:
#         flowers.append(plant)
#     elif "Shrub" in plant:
#         shrubs.append(plant)
# print(flowers)
# print(shrubs)



