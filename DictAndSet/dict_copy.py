import copy

animals = {
    "lion": ["scary", "big", "cat"],
    "elephant": ["big", "grey", "wrinkled"],
    "teddy": ["cuddly", "stuffed"]
}

# things = animals #one way of copying one dict to another and exact copy
# things = animals.copy()  # creates a copy of one to another but both are different and independent(shallow copy)
# animals["teddy"] = "toy"

# perform deep copy
things = copy.deepcopy(animals)
print(things["teddy"])
print(animals["teddy"])

# shallow copy
things["teddy"].append("toy")
print(things["teddy"])
print(animals["teddy"])
