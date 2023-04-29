# list=["Abhinav","Ankit","Vaishali","Sachin"]
# list.append("Beeru")
# list.extend(["mom","papa"])
# print(list[0:4]) #select and print specified element from the list
# # print(list.index("Beeru"))
# # list.insert(2,"Ashish") #insert element before the index
# # list.insert(len(list),"Ritu") # equal to list.append()
# # list.pop(0) #remove the specified element from the index and if not specified then remove the last element from the list
# print(list)
# # Split string method
# names_string = input("Give me everybody's names, separated by a comma. ")
# names = names_string.split(", ")
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇
# a=list(names)
# length=len(a)
# rand=random.randint(0,length-1)
# print(f"{a[rand]} is going to buy the meal today!")
# import random
# names_string = input("Give me everybody's names, separated by a comma. ")
# names = names_string.split(",")
# num_of_items=len(names)
# random_pick_name=random.randint(0,num_of_items-1)
# print(names[random_pick_name])

# fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
# vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
 
# dirty_dozen = [fruits, vegetables]
 
# print(dirty_dozen[1][1])
# print(dirty_dozen)

# print(dirty_dozen[0])
# print(dirty_dozen[1])

# print(dirty_dozen[1][2])
# print(dirty_dozen[1][3])

# # 🚨 Don't change the code below 👇
# row1 = ["⬜️","⬜️","⬜️"]
# row2 = ["⬜️","⬜️","⬜️"]
# row3 = ["⬜️","⬜️","⬜️"]
# map = [row1, row2, row3]
# print(f"{row1}\n{row2}\n{row3}")
# position = input("Where do you want to put the treasure? ")
# # 🚨 Don't change the code above 👆
# #Write your code below this row 👇
# horizontal=int(position[0])
# vertical=int(position[1])
# starting_row=map[vertical-1]
# starting_row[horizontal-1]="X"
# #Write your code above this row 👆

# # 🚨 Don't change the code below 👇
# print(f"{row1}\n{row2}\n{row3}")

##String to List of Strings##
# string1="Python is great"
# #printing the string
# print("Actual String: ",string1)   
# #gives us the type of string1
# print("Type of string: ",type(string1))  
# print("String coverted to list :",string1.split()) 
# #prints the list given by split()

# String to List of Characters
#given string
string1="AskPython" 
#printing the string
print("Actual String: ",string1)
#confirming the type()
print("Type of string: ",type(string1))
#type-casting the string into list using list()
print("String coverted to list :\n",list(string1))

# List of Strings to List of Lists
# string1="This is Python"
# print("The actual string:",string1)
# #converting string1 into a list of strings
# string1=string1.split()
# #applying list method to the individual elements of the list string1
# list1=list(map(list,string1))
# #printing the resultant list of lists
# print("Converted to list of character list :\n",list1)

# CSV to List
# string1="abc,def,ghi"
# print("Actual CSV String: ",string1)
# print("Type of string: ",type(string1))
 
# #spliting string1 into list with ',' as the parameter
# print("CSV coverted to list :",string1.split(','))

# A string consisting of Integers to List of integers
#string with integers sepated by spaces
string1="1 2 3 4 5 6 7 8"
# print("Actual String containing integers: ",string1)
# print("Type of string: ",type(string1))
 
# #coverting the string into list of strings
list1=list(string1.split())
print("Converted string to list : ",list1)
 
# #typecasting the individual elements of the string list into integer using the map() method
# list2=list(map(int,list1))
# print("List of integers : ",list2)