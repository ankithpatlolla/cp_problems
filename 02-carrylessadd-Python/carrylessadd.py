# carry less addition means a  normal addition with the carry from each column ignored.
# So, for example, if we carryless-ly add 8+7, we get 5 (ignore the carry). And if we add
# 18+27, we get 35 (still ignore the carry). With this in mind, write the function
# fun_carrylessadd(x, y) that takes two non-negative integers x and y and returns their
# carryless sum. As the paper demonstrates, fun_carrylessadd(785, 376) returns 51.


def fun_carrylessadd(x, y):
    res = ""
    while x > 0 and y > 0:
        r1, r2 = x % 10, y % 10
        if r1 + r2 < 10:
            res += str(r1 + r2)
        res += str((r1 + r2) % 10)
        x, y = x // 10, y // 10
    return int(res)
