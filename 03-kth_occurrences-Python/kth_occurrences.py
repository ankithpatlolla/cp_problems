# Given a string str and an integer K, the task is to find the K-th most
# frequent character in the string. If there are multiple characters that
# can account as K-th the most frequent character then, print any one of them.


def fun_kth_occurrences(s, n):
    s = s.strip()
    maxi = 0
    res = ''
    for i in s:
        if i != " ":
            if s.count(i) >= maxi:
                maxi = s.count(i)
                res = i
    return res
