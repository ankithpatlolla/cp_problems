# Write the function alternatingSum(L) that takes a possibly-empty list of numbers,
# and returns the alternating sum of the list, where every other value is subtracted
# rather than added. For example: alternatingSum([1,2,3,4,5]) returns 1-2+3-4+5
# (that is, 3). If L is empty, return 0. You may not use loops/iteration in this problem.


def alt(l, i, total):
    if not l or i < len(l):
        return total
    if i % 2 == 0:
        total += l[i]
    else:
        total -= l[i]
    # l.pop(i)
    alt(l, i + 1, total)


def fun_recursions_alternatingsum(l):
    total = 0
    return alt(l, 0, total)
