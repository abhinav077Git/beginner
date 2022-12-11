# numbers = {*""}

numbers = set()
print(numbers, type(numbers))

# numbers.add(1)
# print(numbers)

# while len(numbers) < 4:
#     next_value = input("Please enter your next value: ")
#     if next_value.isnumeric():
#         numbers.add(next_value)
#     else:
#         print("Number is not valid")
# print(numbers)

data = ["blue", "red", "blue", "green", "red", "blue", "white"]
# create set from list to remove duplicates

# unique_data = set(data)
unique_data = sorted(set(data))  # sorted will take anything iterable and produces the list
print(unique_data)

# create list of unique colours, keeping the order they appeared

unique_data = list(dict.fromkeys(data))
print(unique_data)

print()
print(dict.fromkeys(data))
