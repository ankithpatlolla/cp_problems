# digitCount(n)[10pts]
# Write the function digitCount(n) that takes a possibly-negative int and returns the number of digits in it.
# So, digitCount(12323) returns 5, digitCount(0) returns 1, and digitCount(-111) returns 3. One way you
# could do this would be to return len(str(abs(n))), but you cannot do that, since you may not use strings
# here! This can be solved with logarithms, but seeing as this is "loops week", you should instead simply
# repeatedly remove the ones digit until you cannot.

def digitcount(n):
    # your code goes here
    n = abs(n)
    count = 0
    while n >= 0:
        count += 1
        n = n // 10
    return count
