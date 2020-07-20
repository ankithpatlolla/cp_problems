# Write the function hasnoprimes(L) that takes a 2d list L of integers,
# and returns True if L does not contain any primes, and False otherwise.


def is_prime(self, n):
    if n <= 0 or n % 2 == 0 or n % 3 == 0:
        return False
    if n <= 3:
        return True
    else:
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True


def fun_hasnoprimes(l):
    for i in range(len(l)):
        if any(is_prime(l[i][j]) for j in range(len(l[i]))):
            return False
        return True
