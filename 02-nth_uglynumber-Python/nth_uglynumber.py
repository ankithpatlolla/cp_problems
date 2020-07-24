# Write the function nthUglyNumber that takes a non-negative int n and returns the nth Ugly Number.
# Ugly numbers are numbers whose only prime factors are 2, 3 or 5. The sequence 1, 2, 3, 4, 5, 6, 8,
# 9, 10, 12, 15 shows the few ugly numbers. By convention, nthUglyNumber(0) will give 1.

def primes(n, l):
    while n % 2 == 0:
        l.append(2)
        n /= 2
    for i in range(3, int(n ** 0.5) + 1, 2):
        while n % i == 0:
            l.append(i)
            n /= i
    if n > 2:
        l.append(n)
    return l


def is_ugly(n):
    l = primes(n, [])
    if max(l) > 5:
        return False
    return True


def fun_nth_uglynumber(n):
    i = 2
    c = 0
    if n == 0:
        return 1
    while 1:
        if is_ugly(i):
            c += 1
            if c == n:
                break
        i += 1
    return i
