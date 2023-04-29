# def factorial(n:int) -> int:
#     """
#     return integer
#     """
#     product = 1
#     for i in range(n):
#         product = product * (i + 1)
#     return product
#
#
# f = factorial(5)
# print(f)


def factorial(n: int) -> int:
    """Return n! (0! is 1)."""
    if n <= 1:
        return 1

    result = 2
    for x in range(3, n + 1):
        result *= x

    return result


for i in range(35):
    print(i, factorial(i))
