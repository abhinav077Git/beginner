parrot="Norwegian Blue"
print(parrot)
###Indexing
# print(parrot[3])
# print(parrot[4])
# print(parrot[9])
# print(parrot[3])
# print(parrot[6])
# print(parrot[8])
###Negative indexing
# print(parrot[-11])
# print(parrot[-10])
# print(parrot[-5])
# print(parrot[-11])
# print(parrot[-8])
# print(parrot[-6])
###Slicing
# print(parrot[0:6])
# print(parrot[0:9])
# print(parrot[:9])
# print(parrot[10:])
# print(parrot[:])
# print(parrot[:6]+parrot[6:])

# print(parrot[-14:-8])
# print(parrot[-4:-2])
# print(parrot[-4:12])
# print(parrot[-14:-5])
# print(parrot[:-5])
# print(parrot[-14:])
# print(parrot[:])
# print(parrot[:-8]+parrot[-8:])

# ###slicing with step
# print(parrot[0:6:2])
# print(parrot[0:6:3])

###printing the below values in list of integer###
# numbers="9,223;372:036 854,775;807"
# seperators=numbers[1::4]
# print(seperators)

# values="".join(char if char not in seperators else " " for char in numbers).split()
# # print(list(map(int,values)))
# print([int(val) for val in values])

# slicing backwards
# letters="abcdefghijklmnopqrstuvwxyz"
# # print(letters[25::-1])
# # print(letters[::-1])
# print(letters[16:13:-1])
# print(letters[4::-1])
# print(letters[25:17:-1])
# print(letters[:-9:-1])
# print(letters[-4:])
# print(letters[-1:])

data = "1:A, 2:B, 3:C, 4:D, 5:E, 6:F, 7:G, 8:H"
print(data[::5])
print(data[0::5])
print(data[0:-1:5])
print(data[:-1:5])
