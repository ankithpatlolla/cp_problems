# Given a string str and an integer K, the task is to find the K-th most
# frequent character in the string. If there are multiple characters that
# can account as K-th the most frequent character then, print any one of them.


def fun_kth_occurrences(s, n):
    s = s.strip()
    d = {}
    for i in set(s):
        key = s.count(i)
        if key in d:
            d[key].append(i)
        else:
            d[key] = [i]
    maxi = max(d.keys())
    return d[n][0]
