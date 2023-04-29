# # even=[2,4,6,8]
# # odd=[1,3,5,7,9]

# # even.extend(odd)
# # print(even)

# # even.sort()
# # print(even)

# # even.sort(reverse=True)
# # print(even)

# ####sorting method###

# pangram="Hello this is Abhinav Pandey"
# letters=sorted(pangram)
# print(letters)

# numbers=[2.3,4.5,5.6,6.7,7.8]
# sorted_numbers=sorted(numbers) #sorted return new list whereas sort return same list after making changes in that list
# print(sorted_numbers)

# numbers.sort()
# print(numbers)
# another_number=numbers.sort()
# print(another_number) #return None

# names=["Abhinav","Vaishali","beeru","mom","papa","brother","abhinav","vaishali"]
# names.sort(key=str.casefold)##it will sort the name ignoring case sensitivity
# print(names)

# ###creating list###

# creating_list=[]
# even=[2,4,6,8]
# odd=[1,3,5,7,9]

# creating_list=even+odd
# print(creating_list) # creates list

# sorted_creating_list=sorted(creating_list)
# print(sorted_creating_list) #creates list

# digit=sorted("456789231")
# print(digit) #creates list

# # more_creating_list=list(creating_list)# list method to copy list although both are different
# # more_creating_list=creating_list[:]# slice method
# more_creating_list=creating_list.copy()#copy method
# numbers=list("456781239") #convert each character as list of string
# print(numbers)
# print(more_creating_list) 

# print(creating_list is more_creating_list) #return false as they are not same list
# print(creating_list == more_creating_list) # return true as they contains same items

# # adding items to list

# computer_parts=["laptop","Keyboard","mouse","trackball","monitor","dvd drive","cpu"]

# computer_parts[3]="desktop"
# print(computer_parts)

# # computer_parts[3:]="Abhinav" #split the string in list of individual character
# computer_parts[3:]=["Abhinav"]
# print(computer_parts)

#process of removing the low values from the list[only with sorted list]
data=[4,5,104,105,110,120,130,130,150,160,170,183,185,187,188,191,350,360]
min_value=100
stop=0
for index,value in enumerate(data):
    if data[index] >= min_value:
        stop = index
        break
print(stop)
del data[:stop]
print(data)

#process of removing the high values from the list
max_value=200
start=0
for index in range(len(data)-1,-1,-1):
    if data[index] <= max_value:
        start=index +1
        break
print(start)
del data[start:]
print(data)

#############################################################[sorted or unsored list]####################
# removing items from list backwards
num_list=[104,101,4,105,308,103,5,107,100,306,106,102,108]

# for index in range(len(num_list) -1, -1,-1):
#     if (num_list[index] < min_value) or (num_list[index] > max_value):
#         print(index,num_list)
#         del num_list[index]
# print(num_list)

top_index=len(num_list) -1
for index,val in enumerate(reversed(num_list)):
    if val < min_value or val > max_value:
      print(top_index - index, val)
      del num_list[top_index - index]
print(num_list)