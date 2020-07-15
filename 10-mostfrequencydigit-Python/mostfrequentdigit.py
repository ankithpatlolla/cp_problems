# mostFrequentDigit(n) [10pts]
# Write the function mostFrequentDigit(n), that takes a non-negative integer n and returns the digit from 0 to 9
# that occurs most frequently in it, with ties going to the smaller digit.

def mostfrequentdigit(n):
    # your code goes here
    d = {}
    if n == 0:
        return 0
    while n > 0:
        num = n % 10
        if num in d:
            d[num] += 1
        else:
            d[num] = 1
        n = n // 10
    return max(sorted(d.items(), key=lambda x: (
        x[0], x[1])), key=lambda k: k[1])[0]
