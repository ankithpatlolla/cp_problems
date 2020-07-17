# isRotation(x, y) [15 pts]
# Write the function isRotation(x, y) that takes two non-negative integers x and y, both
# guaranteed to not contain any 0's, and
# returns True if x is a rotation of the digits of y and False otherwise. For example,
# 3412 is a rotation of 1234. Any number
# is a rotation of itself.


def num_count(n):
    count = 0
    while n:
        n = n // 10
        count += 1
    return count


def rev(n):
    reversed = 0
    while n:
        rem = n % 10
        reversed = (reversed * 10) + rem
        n = n // 10
    return reversed


def isrotation(x, y):
    # Your code goes here

    if (rev(x) == y):
        return True
    if num_count(x) != num_count(y):
        return False
    digits = num_count(x)
    expo = 10 ** (digits - 1)
    for i in range(digits - 1):
        x = ((x % 10) * expo + (x / 10))
        print(x, "in isRotate")
        if x == y:
            return True
    return False


print(isrotation(10010, 10100))
