from content_quantities import pantry, recipes


# def shopping_list_items(shop_list, shop_item, quantity):
#     shop_list.append((shop_item, quantity))

def shopping_list_items(shop_dict, shop_item, quantity):
    # if shop_item in shop_dict:
    #     shop_dict[shop_item] = shop_dict[shop_item] + quantity
    # else:
    #     shop_dict[shop_item] = quantity
    shop_dict[shop_item] = shop_dict.setdefault(shop_item, 0) + quantity


# print(pantry)
# print(recipes)
dictionary_recipes = {}
for index, key in enumerate(recipes):
    dictionary_recipes[str(index + 1)] = key
# print(dictionary_recipes)
# shopping_list = []
shopping_list = {}
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
        for item, required_quantity in ingredients_selected.items():  # becomes dictionary
            # print(f"your pantry has {item} in {required_quantity} ok")
            quantity_in_pantry = pantry.get(item, 0)
            if required_quantity <= quantity_in_pantry:
                print(f"{item} {quantity_in_pantry} ok")
            else:
                quantity_to_buy = required_quantity - quantity_in_pantry
                print(f"you need to buy {quantity_to_buy} of {item}")
                shopping_list_items(shopping_list, item, quantity_to_buy)

# for things in sorted(shopping_list):
#     print(things)

for things in shopping_list.items():
    print(things)
