# nthAutomorphicNumbers(n) [20 pts]
# In mathematics, an automorphic number is a number whose square "ends" in the same digits as the
# number itself. For example, 5^2 = 25, 6^2 = 36, 76^2 = 5776, and 890625^2 = 793212890625, so 5, 6,
# 76 and 890625 are all automorphic numbers.


def is_automorphic(n):
    x = n * n
    k = 10 ** len(str(n))
    if x % k == n:
        return True
    return False


def nthautomorphicnumbers(n):
    # Your code goes here
    i = 0
    c = 0
    while n != -1:
        if is_automorphic(i):
            c += 1
            if c == n:
                break
        i += 1
    return i
