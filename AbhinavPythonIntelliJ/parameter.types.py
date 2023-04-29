# def func(p1,p2,*args,k,**kargs):
#     print(f"positional-or-keyword....{p1},{p2}")
#     print(f"var-positional(*args)....{args}")
#     print(f"keyword:...{k}")
#     print(f"var-keyword:.....{kargs}")
#
#
# func(1,2,3,4,5,k=6,key1=7,key2=8)


# Values              Result
# 1, 2, 3             6
# 8, 20, 2            30
# 12.5, 3.147, 98.1   113.747
# 1.1, 2.2, 5.5       8.8

def sum_numbers(*args: float) -> float:
    """

    :param args: return the sum of values in tuples and unpack it
     into variable value and make it iterate through variable
    :return:
    """
    # print(args)
    result = 0
    for i in args:
        result = result + i
    return result


print(sum_numbers(1, 2, 3))
print(sum_numbers(8, 20, 2))
print(sum_numbers(12.5, 3.147, 98.1))
print(sum_numbers(1.1, 2.2, 5.5))
