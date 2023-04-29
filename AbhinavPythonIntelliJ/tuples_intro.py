welcome="welcome to my nightmare","alice cooper",1975
bad="bad company","bad company",1974
budgie="nightflight","budgie",1981
imelda="more mayhem","emilda may",2011
metallica="ride the lighting","metallica",1984

# tuples does not support item assignment
print(metallica)

# unpacking tuple

# x,y,z=1,2,3
# print(x)
# print(y)
# print(z)

##unpacking tuple##
title,artist,year=metallica
print(title)
print(artist)
print(year)

# print("unpacking tuple")
# data=1,2,76
# x,y,z=data
# print(x)
# print(y)
# print(z)

# print("unpacking list")
# data_list=[23,34,45]
# x,y,z=data_list
# print(x)
# print(y)
# print(z)

# practical uses of unpacking tuples

# for index,character in enumerate("abcdefgh"):
#     print(index,character)

# for t in enumerate("abcdefgh"):
#     index,character=t #unpacking tuples
#     # print(t)#tuples will be printed for each string and by unpacking above we can get simple output
#     print(index,character)

# index,character=(0,"a")
# print(index)
# print(character)

