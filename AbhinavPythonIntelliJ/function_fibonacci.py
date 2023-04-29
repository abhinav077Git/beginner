# fibonacci series
# return nth fibonacci number for number n
def fibonacci(n):
    if 0 <= n <= 1:
        return n
    nminus1, nminus2 = 1, 0
    result = None
    for f in range(n - 1):
        result = nminus1 + nminus2
        nminus2 = nminus1
        nminus1 = result
    return result


for i in range(36):
    print(i, fibonacci(i))
