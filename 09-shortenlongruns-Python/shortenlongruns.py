# shortenLongRuns(L, k) [15 pts]
# Write the non-destructive function shortenLongRuns(L, k) that takes a list L and a positive integer k, and
# non-destructively returns a similar list, only without any run of k consecutive equal values in L. This means that
# any values that would otherwise produce a consecutive run of k elements are not present.
# For example:
# assert(shortenLongRuns([2, 3, 5, 5, 5, 3], 2) == [2, 3, 5, 3])
# assert(shortenLongRuns([2, 3, 5, 5, 5, 3], 3) == [2, 3, 5, 5, 3])
# Note: your function may not just create a copy of L and call the destructive version of this function (below) on
# that copy and return it. Instead, you must directly construct the result here.


def shortenlongruns(L, k):
    # Your code goes here
    b = []
    count = 0
    i = 0
    prev = L[0]
    while i < len(L):
        while L[i] == prev:
            count += 1
            if count < k:
                b.append(L[i])
            i += 1
            if i == len(L) - 1:
                break
        coount = 0
        b.append(L[i])
        prev = L[i]
        i += 1
    return b


# print(shortenlongruns([2, 3, 5, 5, 5, 3], 3))
