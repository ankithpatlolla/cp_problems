# nthPowerfulNumber(n) [20 pts]
# Write the function nthPowerfulNumber(n). See here for details. So nthPowerfulNumber(0) returns
# 1, and nthPowerfulNumber(10) returns 64.
# A number n is said to be Powerful Number if for every prime factor p of it, p2 also divides it.
# For example:- 36 is a powerful number. It is divisible by both 3 and square of 3 i.e, 9.

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def primes(n, l):
    for i in range(2, n):
        if is_prime(i) and n % i == 0:
            l.append(i)
    return l


def is_powerful(n):
    l = primes(n, [1])
    for i in l:
        if n % (i * i) != 0:
            return False
    return True


def nthpowerfulnumber(n):
    # Your code goes here
    i = 1
    c = 0
    while True:
        if is_powerful(i):
            if c == n:
                break
            c += 1
        i += 1
    return i
