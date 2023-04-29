###checking whether it is Prime#####
def prime_checker(number):
  for i in range (2,number):
    if number % i == 0:
      return False
  return True
n = int(input("Check this number: "))
output=prime_checker(number=n)
print(output)

######################################
def prime_checker(number):
  is_Prime=True
  for i in range (2,number):
    if number % i == 0:
      is_Prime=False
  if is_Prime:
    print("Prime")
  else:
    print("Not Prime")
n = int(input("Check this number: "))
prime_checker(number=n)