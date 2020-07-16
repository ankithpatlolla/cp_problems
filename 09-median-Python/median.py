# median(a) (10 pts)
# Write the non-destructive function median(a) that takes a list of ints or floats and returns the median value,
# which is the value of the middle element, or the average of the two middle elements if there is no single middle
# element. If the list is empty, return None.

def median(a):
    # your code goes here
    n = len(a)
    if n == 0:
        return None
    # elif n % 2 == 0:
    #     return (a[((n - 1) // 2)] + a[(n + 1) // 2]) / 2
    # else:
    #     return a[n // 2]
    return (a[((n - 1) // 2)] + a[(n + 1) // 2]) / 2
