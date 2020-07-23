# Note: please do not start this problem prior to completing previous problem.
# Bearing in mind the definition of Kaprekar Number from above problem, write the function
# nearestKaprekarNumber(n) that takes an int value n and returns the Kaprekar number
# closest to n, with ties going to smaller value. For example, nearestKaprekarNumber(49) returns 45,
# and nearestKaprekarNumber(51) returns 55. And since ties go to the smaller number,
# nearestKaprekarNumber(50) returns 45.
# Note: as you probably guessed, this also cannot be solved by counting up from 0,
# as that will not be efficient enough to get past the autograder.
# Hint: one way to solve this is to start at n and grow in each direction until you find a Kaprekar number..


import math


def is_kap(n):
    num = n ** 2
    k = 0
    while num // (10 ** k) != 0:
        a = num % (10 ** k)
        b = num // (10 ** k)
        if a != 0 and a + b == n:
            return True
        k += 1
    return False


def fun_nearestkaprekarnumber(n):
    forward = n
    backward = n
    while True:
        forward += 1
        backward -= 1
        if is_kap(backward):
            return backward
        if is_kap(forward):
            return forward
