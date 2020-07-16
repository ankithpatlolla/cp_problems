# A happy prime is a number that is both happy and prime.
# Write the function nthHappyPrime(n) which takes a non-negative integer
# and returns the nth happy prime number (where the 0th happy prime number is 7).

def sum_num(n):
    total = 0
    while n:
        total += (n % 10) ** 2
        n = int(n / 10)
    return total


def ishappynumber(n):
    # your code goes here
    if n == 1:
        return True
    elif n == 0 or n == 4:
        return False
    else:
        while True:
            check = sum_num(n)
            return ishappynumber(check)


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def fun_nth_happy_prime(n):
    count = -1
    i = 1
    while True:
        if ishappynumber(i) and is_prime(i):
            count += 1
            if count == n:
                return i
        i += 1
