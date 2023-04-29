# empty_list=[]
# even=[2,4,6,8]
# odd=[1,3,5,7,9]

# numbers=[even,odd]

# for number_list in numbers:
#     print(number_list)

#     for number in number_list:
#         print(number)



names=["abhinav","ankit"]
# print(names.index("abhinav"))
# menu=[["egg","bacon"],
#   ["egg","sausage","bacon"],
#   ["egg","spam"],
#   ["egg","bacon","spam"],
#   ["egg","bacon","sausage","spam"],
#   ["spam","sausage","spam","bacon"],
#   ["spam","egg","spam","bacon","spam"]
# ]
# print(menu)

# for menu_list in menu:
#     if "spam" not in menu_list:
#         print(menu_list)

#         for item in menu_list:
#             print(item)
#     else:
#         print(f"menu has spam count as:{menu_list.count('spam')} in {menu_list}")

###program to print list with no spam in every sublist###
menu=[["egg","bacon"],
  ["egg","sausage","bacon"],
  ["egg","spam"],
  ["egg","bacon","spam"],
  ["egg","bacon","sausage","spam"],
  ["spam","sausage","spam","bacon"],
  ["spam","egg","spam","bacon","spam"]
]

# for meal in menu:
#     for index in range(len(meal) -1,-1,-1):
#         # print(index)
#         if meal[index]=="spam":
#             del meal[index]
#     print(meal)


for meal in menu:
    for item in meal:
        if item != "spam":
            print(item,end=" ")
    print()

# modified_menu=[]
# for index_item in range(len(menu)):
#     if "spam" in menu[index_item]:
#         # print(index_item)
#         sub_list=[]
#         for item in menu[index_item]:
#             if "spam" not in item:
#               sub_list.append(item)
#         # print(sub_list)

#         modified_menu.append(sub_list)
#     else:
#         modified_menu.append(menu[index_item])
# print(modified_menu)

