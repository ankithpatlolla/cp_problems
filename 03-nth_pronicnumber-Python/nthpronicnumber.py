# nthPronicNumber(n) [20 pts]
# Write the function nthPronicNumber that takes a non-negative int n and returns the nth Pronic
# Number. Pronic number is a number which is the product of two consecutive integers, that is, a
# number n is a product of x and (x+1).


def nthpronicnumber(n):
    # Your code goes here
    i = 1
    c = 0
    res = 0
    while 1:
        if c == n:
            break
        res = i * (i + 1)
        c += 1
        i += 1
    return res
