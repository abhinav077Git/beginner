# We need an empty dictionary, to store and display the letter frequencies.
word_count = {}

# Text string
text = "Later in the course, you'll see how to use the collections Counter class."

# Your code goes here ...
for char in text.casefold():
    if char.isalnum():  # we are only counting letter and digit
        if char in word_count:
            word_count[char] = word_count[char] + 1
        else:
            word_count[char] = 1
        # word_count[char] = word_count.setdefault(char,0) + 1

print(word_count)

# Printing the dictionary
for letter, count in sorted(word_count.items()):
    print(letter, count)
