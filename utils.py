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


def power_of_5(a):
    while a > 1:
        if a % 5 == 0:
            a //= 5

        else:
            return False

    return True

