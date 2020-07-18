# Given a string str and an integer K, the task is to find the K-th most
# frequent character in the string. If there are multiple characters that
# can account as K-th the most frequent character then, print any one of them.


def fun_kth_occurrences(s, n):
    s = s.strip()
    l = []
    for i in s:
        if ((s.count(i), i)) not in l and i != " ":
            l.append((s.count(i), i))
    l.sort(key=lambda x: x[0], reverse=True)
    # print(l)
    try:
        return l[n-1][1]
    except:
        return l[0][1]

# print(fun_kth_occurrences("hsdibdouvbeiovbfeibvdsioubidsbvviefadbcildfab", 4))
