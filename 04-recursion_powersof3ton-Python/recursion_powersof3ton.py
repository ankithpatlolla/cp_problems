# Recursion-Only powersOf3ToN(n) [15 pts]
# Write the function powersOf3ToN(n) that takes a possibly-negative float or int n, and returns a list of the
# positive powers of 3 up to and including n. As an example, powersOf3ToN(10.5) returns [1, 3, 9]. If no such powers
# of 3 exist, you should return the empty list. You may not use loops/iteration in this problem.

def powers(n, l, p):
    if p ** 2 >= n or p <= 0:
        return l
    l.append(p ** 2)
    return (n, l, p + 2)


def recursion_powersof3ton(n):
    # Your code goes here
    return powers(n, [], 1)
