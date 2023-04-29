alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
from art import logo
print(logo)
#####beginner level code######
# def encrypt(plain_text,shift_amount):
#     end_text=""
#     for char in text:
#         if char in alphabet:
#             position=alphabet.index(char)
#             new_position=position+shift
#             end_text=end_text+alphabet[new_position]
#     print(f"encoded string is {end_text}")

# def decrypt(cipher_text,shift_amount):
#     plain_text=""
#     for char in text:
#         if char in alphabet:
#             position=alphabet.index(char)
#             new_position=position-shift
#             plain_text=plain_text+alphabet[new_position]
#     print(f"decoded string is {plain_text}")

# if direction == "encode":
#     encrypt(plain_text=text,shift_amount=shift)
# else:
#     decrypt(cipher_text=text,shift_amount=shift)

##########################################################
# print(string.index("h"))
# generated_char=""
# for char in string:
#     if char in alphabet:
#         i=alphabet.index(char)
#         i=i+5
#         # generated_char=alphabet[i]
#         generated_char=generated_char+alphabet[i]
# print(generated_char)

# new_char=""
# for char in string:
#     position=alphabet.index(char)
#     i=5
#     new_position=position+i
#     new_char=new_char+alphabet[new_position]
# print(new_char)

###############advanced level##################
def caesar(caesar_plain_text,caesar_shift_amount,caesar_direction):
    end_text=""
    for char in text:
        if char in alphabet:
            position=alphabet.index(char)
            if caesar_direction == "encode":
                new_position=position+shift
                end_text=end_text+alphabet[new_position]
            else:
                new_position=position-shift
                end_text=end_text+alphabet[new_position]
        else:
            end_text=end_text+char
    print(f"{caesar_direction}d string is {end_text}")

should_continue=True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26
    caesar(caesar_plain_text=text,caesar_shift_amount=shift,caesar_direction=direction)
    result=input("want to continue : Type: Yes or No ")
    if result == "No":
        should_continue=False
        print("Good Bye!!")

########################################################################33

