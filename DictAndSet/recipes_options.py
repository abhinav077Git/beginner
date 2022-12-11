recipes_tuple = {
    "Chicken and chips": [
        ("chicken", 100),
        ("potatoes", 3),
        ("salt", 1),
        ("malt vinegar", 5),
    ],
}

print("print for list of tuples inside dictionary")
for key, value in recipes_tuple.items():
    recipe_key_tuple = recipes_tuple[key]
    # print(recipe_key_tuple)
    print(f"Ingredient for recipe: {key}")
    for ingredients in recipe_key_tuple:
        ingredient, quantity = ingredients
        print(ingredient, quantity, sep=", ")
print("===============================================")
print("printing the list of dictionary inside dictionary ")
recipes_dict = {
    "Chicken and chips": {
        "chicken": 100,
        "potatoes": 3,
        "salt": 1,
        "malt vinegar": 5,
    },
}

# one way of doing it for dictionary of dictionary
# recipes_key_dict = {}
# for index, recipe in enumerate(recipes_dict):  # create tuples of index,value of one element in dictionary
#     recipes_key_dict[str(index + 1)] = recipe
#     for key, value in recipes_key_dict.items(): # use that value from above tuple as key to iterate through dictionary
#         selected_key_value = recipes_dict[value]
#         print(f"Ingredient for recipe: {value}")
#         for ingredient, quantity in selected_key_value.items():
#             print(ingredient, quantity, sep=", ")
# second way of doing it for dictionary to dictionary
for recipe, items in recipes_dict.items():
    selected_key_value = recipes_dict[recipe]
    # print(selected_key_value)
    print(f"Ingredient for recipe: {recipe}")
    for ingredient, quantity in selected_key_value.items():
        print(ingredient, quantity, sep=", ")
