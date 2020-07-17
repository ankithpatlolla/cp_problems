# Write the function fun_isfactorish(n) that takes a value int n,
# and returns True if n is a (possibly-negative) integer with exactly 3 unique digits
# (so no two digits are the same), where each of the digits is a factor of the number
# n itself. In all other cases, the function returns False (without crashing).
# For example:
#  assert(fun_isfactorish(412) == True) # 4, 1, and 2 are all factors of 412
#  assert(fun_isfactorish(-412) == True) # Must work for negative numbers!
#  assert(fun_isfactorish(4128) == False) # 4128 has more than 3 digits
#  assert(fun_isfactorish(112) == False) # 112 has duplicate digits (two 1's)
#  assert(fun_isfactorish(420) == False) # 420 has a 0 (0 is not a factor)
#  assert(fun_isfactorish(42) == False) # 42 has a leading 0 (only 2 unique digits)

def is_uniqe(n):
    l = []
    while n:
        if n % 10 in l:
            return False
        l.append(n % 10)
        n = int(n / 10)
    return True


def fun_isfactorish(n):
    if len(str(n)) != 3 or not is_uniqe(n):
        return False
    n = abs(n)
    while n:
        if n % 10 == 0:
            return False
        if n % (n % 10) != 0:
            return False
        n = int(n / 10)
    return True
