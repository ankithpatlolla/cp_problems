# Write the function rotatestring(s, k) that takes a string s and a possibly-negative integer k.
# If k is non-negative, the function returns the string s rotated k places to the left.
# If k is negative, the function returns the string s rotated |k| places to the right. So, for example:
# assert(rotateString('abcd',  1) == 'bcda')
# assert(rotateString('abcd', -1) == 'dabc')


def fun_rotatestrings(s, n):
    res = s
    if n < 0:
        for i in range(abs(n)):
            res = res[-1] + res[:-1]
        return res
    else:
        for i in range(n):
            res = res[1:] + res[0]
        return res
