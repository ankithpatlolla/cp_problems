# Without using the builtin method s.replace(),
# write its equivalent. Specifically, write the function
# replace(s1, s2, s3) that returns a string equal to
# s1.replace(s2, s3), but again without calling s.replace().


def fun_replace(s1, s2, s3):
    res = ""
    for i in range(len(s1)):
        check = s1[i]
        j = i + 1
        while j < len(s1):
            check += s1[j]
            if len(check) == len(s2):
                break
            j += 1
        if check == s2:
            res += s1[:i] + s3 + s1[j + 1:]
            return res
