def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        print("Calling factorial on {}".format(n-1))
        return n * fact(n-1)

def factorial(n):
    total = 1
    for i in range(1, n+1):
        total *= i
    return total
