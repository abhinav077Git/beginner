small_ints = set(range(21))
print(small_ints)

# small_ints.clear()
# print(small_ints)

small_ints.discard(10)
small_ints.remove(11)
print(small_ints)

small_ints.discard(99)
print(small_ints)  # will not throw error if item does not exist
small_ints.remove(99)
print(small_ints)   # throw error if it does not exist
