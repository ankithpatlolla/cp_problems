# Background: a Kaprekar number is a non-negative integer, the representation of whose square
# can be split into two possibly-different-length parts (where the right part is not zero)
# that add up to the original number again. For instance, 45 is a Kaprekar number, because
# 45**2 = 2025 and 20+25 = 45. You can read more about Kaprekar numbers here. The first several
# Kaprekar numbers are: 1, 9, 45, 55, 99, 297, 703, 999 , 2223, 2728,...
# With this in mind, write the function nthKaprekarNumber(n) that takes a non-negative int n
# and returns the nth Kaprekar number, where as usual we start counting at n==0.


import math


def is_kap(n):
    num = n ** 2
    k = 0
    x = num
    while x > 0:
        a = num % (10 ** k)
        b = num // (10 ** k)
        if a != 0 and a + b == n:
            return True
        k += 1
        x //= 10
    return False


def fun_nth_kaprekarnumber(n):
    i = 0
    while n >= 0:
        if is_kap(i):
            n -= 1
        i += 1
    return i
