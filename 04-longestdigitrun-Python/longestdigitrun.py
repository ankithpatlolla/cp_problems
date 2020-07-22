# longestDigitRun(n) [20 pts]
# Write the function longestDigitRun(n) that takes a possibly-negative int value n and returns
# the digit that has the longest consecutive
# run, or the smallest such digit if there is a tie. So, longestDigitRun(117773732) returns 7 (
# because there is a run of 3 consecutive 7's),
# as does longestDigitRun(-677886).
def longestdigitrun(n):
    # Your code goes here
    most = 0
    maxi = 0
    prev = n % 10
    n //= 10
    c = 1
    while n > 0:
        i = n % 10
        if i == prev:
            c += 1
            if c >= maxi:
                maxi = c
                most = i
        else:
            c = 1
            prev = i
        n //= 10
    return most
