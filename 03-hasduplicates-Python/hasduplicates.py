# hasDuplicates(L) [15 pts]
# Write the function hasDuplicates(L) that takes a 2d list L of arbitrary values, and returns True if L
# contains any duplicate values (that is,
# if any two values in L are equal to each other), and False otherwise.

def hasduplicates(L):
    # Your code goes here
    a = []
    for i in range(len(L)):
        a.extend(L[i])
    s = ''.join(map(str, a))
    if len(str(s)) != len(set(str(s))):
        return True
    return False
