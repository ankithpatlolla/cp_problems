# Without using iteration and without using strings,
# write the recursive function onlyEvenDigits(L),
# that takes a list L of non-negative integers
# (you may assume that), and returns a new list of
# the same numbers only without their odd digits
# (if that leaves no digits, then replace the number with 0).
# So: onlyEvenDigits([43, 23265, 17, 58344]) returns [4, 226, 0, 844].
# Also the function returns the empty list if the original list is empty.
# Remember to not use strings. You may not use loops/iteration in this problem.

def even(n):
    if n == 0:
        return 0
    rem = n % 10
    n = n // 10
    if rem % 2 == 0:
        return even(n) * 10 + rem
    return even(n)


def even_digits(l, res):
    if l == [] or not l:
        return res
    num = l.pop(0)
    res.append(even(num))
    return even_digits(l, res)


def fun_recursion_onlyevendigits(l):
    res = []
    return even_digits(l, res)
