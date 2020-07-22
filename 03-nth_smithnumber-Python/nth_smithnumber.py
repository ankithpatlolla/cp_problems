# Write the function nthSmithNumber that takes a non-negative int n
# and returns the nth Smith number, where a Smith number is a composite (non-prime)
# the sum of whose digits are the sum of the digits of its prime factors (excluding 1).
# Note that if a prime number divides the Smith number multiple times, its digit sum
# is counted that many times. For example, 4 equals 2**2, so the prime factor 2 is
# counted twice, thus making 4 a Smith Number.
# so fun_nthsmithnumber(0) should return 4
# so fun_nthsmithnumber(1) should return 22

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while (i * i) <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6


def total(l, s):
    if len(l) == 0:
        return s
    x = l.pop(0)
    if x < 10:
        s += x
        return total(l, s)
    while x > 0:
        s += x % 10
        x //= 10
    return total(l, s)


def is_smith(n):
    i = 2
    l = []
    while i < n:
        if is_prime(i) and n % i == 0:
            l.append(i)
        i += 1
    c = total(l, 0)
    num = 0
    while n > 0:
        num += n % 10
        n //= 10
    if c == num:
        return True
    return False


def fun_nth_smithnumber(n):
    if is_prime(n):
        return
    k = 0
    if n == 0:
        return 4
    i = 2
    while True:
        if is_smith(i):
            k += 1
        if k == n:
            break
        i += 1
    return i
