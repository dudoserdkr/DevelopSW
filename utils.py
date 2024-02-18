def factorial(a):
    if a == 1 or a == 0:
        return 1
    else:
        return a * (a-1)


def isprime(a):
    sqrt = int(a ** 0.5)

    for i in range(2, sqrt + 1):
        if a % i == 0:
            return False


