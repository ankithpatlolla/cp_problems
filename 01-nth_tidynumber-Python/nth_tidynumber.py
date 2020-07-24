# Write the function nthTidyNumber that takes a non-negative int n and returns the nth Tidy Number.
# A tidy number is a number whose digits are in non-decreasing order.
# fun_nth_tidynumber(0) = 1
# fun_nth_tidynumber(1) = 2
# fun_nth_tidynumber(5) = 6
# fun_nth_tidynumber(15) = 17
# fun_nth_tidynumber(35) = 46

def is_tidy(n):
    prev = n % 10
    n //= 10
    while n > 0:
        x = n % 10
        if x > prev:
            return False
        n //= 10
        prev = x
    return True


def fun_nth_tidynumber(n):
    i = 1
    c = 0
    while True:
        if is_tidy(i):
            if c == n:
                break
            c += 1
        i += 1
    return i
