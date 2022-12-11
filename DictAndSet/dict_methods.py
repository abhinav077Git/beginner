d = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    "iv": "four",
}

d2 = {
    7: "The lucky seven",
    10: "Ten",
    3: "this is the new three"
}

pantry_items = ['chicken', 'spam', 'egg', 'bread', 'lemon']

v = d.values()
print(v)

d[10] = "ten"
print(v)
print("four" in v)
print("eleven" in v)

keys = list(d.keys())  # list of keys
print(keys)
values = list(v)  # list(d.values()) # list of values
print(values)

if "four" in values:
    index = values.index("four")
    key = keys[index]
    print(f"{d[key]} was found with the key: {key}")

print("----------------------------------")

for key, value in d.items():
    if value == "four":
        print(f"{d[key]} was found with the key: {key}")
# code below for update method
# d.update(d2) # updating dictionary with another
# for key, value in d.items():
#     print(key, value)
# print("------------------------------------------------------")
# pantry_items = ['chicken', 'spam', 'egg', 'bread', 'lemon']
# d.update(enumerate(pantry_items))  # update method in dict uses enumerate to iterate through iterable
#
# for key, value in d.items():
#     print(key, value)

# code for remaining `dict` method
# pantry_items = ['chicken', 'spam', 'egg', 'bread', 'lemon']
# new_dict = dict.fromkeys(pantry_items, 0)
# print(new_dict)
#
# keys = d.keys()
# print(keys)
#
# for item in d.keys():
#     print(item)
