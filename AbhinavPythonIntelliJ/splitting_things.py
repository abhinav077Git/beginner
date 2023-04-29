from re import A


panagram="the quick brown fox jumps over the lazy dog"
# print(panagram.split())

numbers="9,223,445,667,546,877,987"
# print(numbers.split(','))

generated_list=["9"," ",
"2","2","3"," ",
"4","4","5"," ",
"6","6","7"," ",
"5","4","6"," ",
"8","7","7"," ",
"9","8","7"]

names="".join(generated_list) #produces string
# print(names)
new_list=names.split() #produces list

# int_list=[]
# for value in new_list:
#     int_list.append(int(value)) #list with set of integers
# print(int_list)

#below also produces list of integer
# for index in range(len(new_list)):
#     new_list[index]=int(new_list[index])
# print(new_list)


#taking input seperated by "," and convert into list and then calculate formula
# input_string=input("Enter the values of a,b and c seperated by comma: ")
# input=input_string.split(",")
# for index in range(len(input)):
#     if index == 0:
#         a=input[index]
#     elif index == 1:
#         b=input[index]
#     else:
#         c=input[index]
# print(int(a)+int(b)-int(c))

# Take input from the user
user_input = input("Please enter three numbers: ")

# Split the given input string into 3 parts
string_tokens = user_input.split(",")

# Convert the tokens into integers
int_tokens = []
for st in string_tokens:
    int_tokens.append(int(st))

# Calculate the result: a + b - c
a, b, c = int_tokens
result = a + b - c
# result = int_tokens[0] + int_tokens[1] - int_tokens[2]

# Output the result
print(result)


