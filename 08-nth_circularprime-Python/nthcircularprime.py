# nthCircularPrime(n) [20 pts]
# Write the function nthCircularPrime that takes a non-negative int n and returns the nth
# Circular prime, which is a prime number that does not contain any 0's and such that all the
# numbers resulting from rotating its digits are also prime. The first Circular primes are 2, 3,
# 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, 97, 113, 131, 197... To see why 197 is a Circular prime,
# note that 197 is prime, as is 971 (rotated left), as is 719 (rotated left again)..

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


def is_circular(n):
    if is_prime(n) == False:
        return False
    num = 0
    digits = len(str(n))
    k = 10 ** (digits - 1)
    i = 0
    while i < digits - 1:
        rem = n // k
        if n % 10 == 0:
            return False
        num = ((n * 10) + rem - (rem * k * 10))
        if n == num or is_prime(num) == False:
            return False
        n = num
        i += 1
    return True


def nthcircularprime(n):
    # Your code goes here
    i = 1
    while n > 0:
        i += 1
        if is_circular(i):
            n -= 1
    return i


# print(is_circular(19))
# print(nthcircularprime(5))
