from content_quantities import recipes


def my_recipes_deepcopy(d):
    new_dict = {}
    for key, value in d.items():
        new_value = value.copy()
        new_dict[key] = new_value
    return new_dict


recipes_copy = my_recipes_deepcopy(recipes)
recipes_copy["Butter chicken"]["ginger"] = 300
print(recipes["Butter chicken"]["ginger"])  # original dictionary
print(recipes_copy["Butter chicken"]["ginger"])  # copied dictionary
