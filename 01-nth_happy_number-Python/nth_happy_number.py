# Write the function nthHappyNumber(n) which takes a non-negative integer
# and returns the nth happy number (where the 0th happy number is 1).
# Here are some test assertions for you:
# assert(nthHappyNumber(0) == 1)
# assert(nthHappyNumber(1) == 7)
# assert(nthHappyNumber(2) == 10)
# assert(nthHappyNumber(3) == 13)
# assert(nthHappyNumber(4) == 19)
# assert(nthHappyNumber(5) == 23)
# assert(nthHappyNumber(6) == 28)
# assert(nthHappyNumber(7) == 31)


def sum_num(n):
    total = 0
    while n:
        total += (n % 10) ** 2
        n = int(n / 10)
    return total


def ishappynumber(n):
    # your code goes here
    if n == 1:
        return True
    elif n == 0 or n == 4:
        return False
    else:
        while True:
            check = sum_num(n)
            return ishappynumber(check)


def fun_nth_happy_number(n):
    count = -1
    i = 1
    while True:
        if ishappynumber(i):
            count += 1
            if count == n:
                return i
        i += 1
