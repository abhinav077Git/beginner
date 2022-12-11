vehicles = {
    'dream': 'Honda 250T',
    'er5': 'Kawasaki ER5',
    'can-am': 'Bombardier Can-Am 250',
    'virago': 'Yamaha XV250',
    'tenere': 'Yamaha XT650',
    'jimny': 'Suzuki Jimny 1.5',
    'fiesta': 'Ford Fiesta Ghia 1.4',
    'roadster': 'Triumph Street Triple'
}

# my_car = vehicles['fiesta']
# print(my_car)
#
# commuter = vehicles['virago']
# print(commuter)
#
# learner=vehicles.get("er5")
# print(learner)

# for key in vehicles:
#     print(key,vehicles[key],sep=", ")

vehicles["starfighter"] = "Lockheed F-104"
vehicles["learjet"] = "Bombardier Learjet 75"
vehicles["toy"] = "glider"
# upgrade the virago
vehicles["virago"] = "Yamaha XV535"

# deleting keys
del vehicles["starfighter"]

# del vehicles["f1"]  # return error when key does not exist
# vehicles.pop("f1")  # return error when key does not exist

vehicles.pop("f1", None)  # return no error(pop method remove an item from the dictionary and return the value)

# result=vehicles.pop("f1", None)
result=vehicles.pop("f1", "You wish! sell the learjet and you might afford a racing car")
print(result)
plane=vehicles.pop("learjet")
print(plane)

bike=vehicles.pop("tenere","not present") #pop method return default value when key does not exist in dictionary else return the value of key
print(bike)
print()

for key, value in vehicles.items():
    print(key, value, sep=", ")
