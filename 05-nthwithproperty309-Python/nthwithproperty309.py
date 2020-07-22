# nthWithProperty309(n) [20 pts]
# We will say that a number n has "Property309" if its 5th power contains every
# digit (from 0 to 9) at least once. 309 is the smallest number with this property.
# Write the function nthWithProperty309 that takes a non-negative int n and returns
# the nth number with Property309.


def is_prop360(n):
    l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    x = (n ** 5)
    while x > 0:
        if n % 10 in l:
            l.remove(n % 10)
        n //= 10
    if len(l) == 0:
        return True
    return False


def nthwithproperty309(n):
    # Your code goes here
    c = 0
    i = 309
    while True:
        if is_prop360(i):
            c += 1
            if c == n:
                break
        i += 1
    return i
