# nthLychrelNumber(n) [20 pts]
# A Lychrel number is a natural number that cannot form a palindrome through the iterative process of
# repeatedly reversing its digits and adding the resulting numbers. This process is sometimes called the
# 196-algorithm, after the most famous number associated with the process.
# The first few Lychrel numbers are 196, 295, 394, 493, 592, 689, 691, 788, 790, 879, 887….

def rev(n):
    res = 0
    while n > 0:
        rem = n % 10
        res = 10 * res + rem
        n //= 10
    return res


def is_pal(n):
    return str(n) == str(n)[::-1]


def is_lychrel(n):
    for i in range(25):
        if is_pal(rev(n) + n):
            return False
        n += rev(n)
    return True


def nthlychrelnumbers(n):
    # your code goes here
    i = 195
    while n > 0:
        i += 1
        if is_lychrel(i):
            n -= 1
    return i


print(nthlychrelnumbers(2))
