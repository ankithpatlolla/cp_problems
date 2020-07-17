# Write the function fun_nth_palindromic_prime(n) that takes a non-negative int n
# and returns the nth palindromic Prime, which is a palidrome number such that
# it is also a prime. For example, 313 is a palindrome and it is prime
# so 313 is an palindrome Prime. fun_nth_palindrome_prime(0) returns 2

def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def is_pal(n):
    rev = 0
    while n:
        rem = n % 10
        rev = (rev * 10) + rem
        n = n // 10
    return rev == n


def fun_nth_palindromic_prime(n):
    count = 0
    for i in range(n):
        if is_prime(i) and is_pal(i):
            if count == n:
                return i
        count += 1
