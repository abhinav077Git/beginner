def sum_oe(n,t):
    sum=0
    if t =="e":
      for i in range(1,n+1):
        if i % 2 == 0:
          print(i)
          sum = sum + i
    elif t =="o":
        for i in range(1,n):
            if i % 2 !=0:
              print(i)
              sum = sum + i
    else:
        return -1
    return sum


# n=int(input("Enter number: "))
# choice=input("enter string to check sum for odd and even: 'e' or 'o': ")
# sum_oe(n,choice)

def sum_eo(n,t):
    sum=0
    if t =="e":
      for i in range(1,n+1):
        if i % 2 == 0:
          sum = sum + i
    elif t =="o":
        for i in range(1,n):
            if i % 2 !=0:
              sum = sum + i
    else:
        return -1
    return sum
n=int(input("Enter number: "))
choice=input("enter string to check sum for odd and even: 'e' or 'o': ")
result=sum_eo(10,choice)
print(result)

# def sum_eo(n, t):
#     """Sum even or odd numbers in range.

#     Return the sum of even or odd natural numbers, in the range 1..n-1.

#     :param n: The endpoint of the range. The numbers from 1 to n-1 will be summed.
#     :param t: 'e' to sum even numbers, 'o' to sum odd numbers.
#     :return: The sum of the even or odd numbers in the range.
#             Returns -1 if `t` is not 'e' or 'o'.
#     """
#     if t == "e":
#         start = 2
#     elif t == 'o':
#         start = 1
#     else:
#         return -1

#     return sum(range(start, n, 2))


# x = sum_eo(11, 'e')
# print(x)

