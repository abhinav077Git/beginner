from contents import pantry, recipes

# print(pantry)
# print(recipes)
dictionary_recipes = {}
for index, key in enumerate(recipes):
    dictionary_recipes[str(index + 1)] = key
# print(dictionary_recipes)

while True:
    print("Please choose from recipes:")
    print("---------------------------")
    for key, value in dictionary_recipes.items():
        print(f"{key}: {value}")

    choice = input()
    if choice == "0":
        break
    elif choice in dictionary_recipes:
        selected_item = dictionary_recipes[choice]
        print(f"You have selected {selected_item}")
        print(f"Checking ingredients........")
        ingredients_selected = recipes[selected_item]
        print(ingredients_selected)
        for item in ingredients_selected:
            if item in pantry:
                print(f"\tYour pantry has {pantry[item]} {item} ok")
            else:
                print(f"\tYou dont have necessary ingredients :{item}")
