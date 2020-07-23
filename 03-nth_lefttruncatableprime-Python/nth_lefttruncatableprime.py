# Write the function nthLeftTruncatablePrime(n).
# A Left-truncatable prime is a prime which in a given base (say 10) does not contain 0
# and which remains prime when the leading (left) digit is successively removed.
# For example, 317 is left-truncatable prime since 317, 17 and 7 are all prime.
# There are total 4260 left-truncatable primes.
# So nthLeftTruncatablePrime(0) retunearestKaprekarNumber(n)rns 2, and
# nthLeftTruncatablePrime(10) returns 53.


import math


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


def is_leftprime(n):
    if not is_prime(n):
        return False
    new = 0    
    while n > 0:
        new += (new * 10) + n % 10
        n //= 10
    new = new % 10
    while new > 0:
        rem = new % 10
        if not is_prime(rem):
            return False
        new //= 10
    return True            
        


def fun_nth_lefttruncatableprime(n):
    i = 2
    if n == 0:
        return 2
    while n > 0:
        i += 1
        if is_leftprime(i):
            n -= 1
    return i
