# Here we will rewrite the previous function to be destructive. This version must not just call the nondestructive
# version from above and then clear and replace the values in the original list. Instead, you must traverse the list
# once and make the changes to the list as you go. With that in mind, write the destructive function shortenLongRuns(
# L, k) that takes a list L and a positive integer k, and destructively modifies L by removing any values in L that
# would otherwise produce a run of k consecutive equal values in L.
# For example:
# L = [2, 3, 5, 5, 5, 3]
# shortenLongRuns(L, 2)
# assert(L == [2, 3, 5, 3])
# And:
# L = [2, 3, 5, 5, 5, 3]
# shortenLongRuns(L, 3)
# assert(L == [2, 3, 5, 5, 3])

def destructiveshortenlongruns(L, k):
    # Your code goes here
    count = 1
    prev = L[0]
    i = 1
    while i < len(L):
        while L[i] == prev:
            count += 1
            if count == k:
                i -= 1
                L.pop(i)
                count -= 1
            if i == len(L) - 1:
                break
            i += 1
        count = 1
        prev = L[i]
        i += 1
    return L


print(destructiveshortenlongruns([2, 3, 5, 5, 5, 3], 3))
