# Without using the builtin method s.replace(),
# write its equivalent. Specifically, write the function
# replace(s1, s2, s3) that returns a string equal to
# s1.replace(s2, s3), but again without calling s.replace().


def fun_replace(s1, s2, s3):
    res = ""
    for i in range(len(s1)):
        check = s1[i]
        for j in range(i, len(s1)):
            check += s1[j]
            if check == s2:
                res += s1[:i] + s1[i:j] + s1[j:]
                return res
