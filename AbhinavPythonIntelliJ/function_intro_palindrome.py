def multiply():
    result=7*6
    return result


answer=multiply()
print(answer)

def multiply1(x,y):
    result=x*y
    return result

answer1=multiply1(5,6)
print(answer1)

for i in range(1,5):
    result=multiply1(i,2)
    print(result)

############function with parameter(checking for palindrome string###############
def is_palindrome(string):
    backwards=string[::-1]# to reverse the string
    return backwards.casefold() == string.casefold()

# string_check=input("Enter string: ")
# print(string_check)
# if is_palindrome(string_check):
#     print(f"{string_check}: It is palindone")
# else:
#     print(f"{string_check}: It is not palindrone")

##############function with parameter(checking for palindrome in sentence)######
# def palindrome_sentence(sentence):
#     string=""
#     for char in sentence:
#         if char.isalnum():
#             string=string+char
#     print(string)

#     backwards=string[::-1]
#     print(backwards)
#     if backwards.casefold() == string.casefold():
#         return backwards

# do geese see god?
# was it a car or a cat , I saw?
# radar,racecar,python
# sentence_check=input("Enter sentence: ")
# if palindrome_sentence(sentence_check):
#     print(f"{sentence_check}: It is palindone")
# else:
#     print(f"{sentence_check}: It is not palindrone")

###################function calling function#############
def palindrome_sentence(sentence):
    string=""
    for char in sentence:
        if char.isalnum():
            string=string+char
    print(string)

    return is_palindrome(string)

# do geese see god?
# was it a car or a cat , I saw?
# radar,racecar,python
sentence_check=input("Enter sentence: ")
if palindrome_sentence(sentence_check):
    print(f"{sentence_check}: It is palindone")
else:
    print(f"{sentence_check}: It is not palindrone")




