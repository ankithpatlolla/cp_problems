# nthPowerfulNumber(n) [20 pts]
# Write the function nthPowerfulNumber(n). See here for details. So nthPowerfulNumber(0) returns
# 1, and nthPowerfulNumber(10) returns 64.
# A number n is said to be Powerful Number if for every prime factor p of it, p2 also divides it.
# For example:- 36 is a powerful number. It is divisible by both 3 and square of 3 i.e, 9.


def primes(x, l):
    while x % 2 == 0:
        l.append(2)
        x = x // 2
    for i in range(3, int((x * 0.5) + 1), 2):
        while x % i == 0:
            l.append(i)
            x = x // i
    if x > 2:
        l.append(x)


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
