# Happy Primes [20 pts]
# Background: read the first paragraph from the Wikipedia page on happy numbers. After
# some thought, we see that no matter what number we start with, when we keep replacing
# the number by the sum of the squares of its digits, we'll always either arrive at 4 (
# unhappy) or at 1 (happy). With that in mind, we want to write the function nthHappyNumber
# (n). However, to write that function, we'll first need to write isHappyNumber(n) (
# right?). And to write that function, we'll first need to write sumOfSquaresOfDigits(n).
# And that's top-down design! Here we go....
# Note: the autograder will grade each of the following functions, so they are required.
# However, they also are here specifically because they are just the right helper
# functions to make nthHappyNumber(n) easier to write!

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def sumOfSquaresOfDigits(n):
    total = 0
    while n > 0:
        total += (n % 10) ** 2
        n = int(n / 10)
    return total


def is_happy(n):
    if n == 1:
        return True
    if n == 0 or n == 4:
        return False
    while True:
        check = sumOfSquaresOfDigits(n)
        return is_happy(check)


def ishappyprimenumber(n):
    # Your code goes here
    if is_prime(n) and is_happy(n):
        return True
    return False
