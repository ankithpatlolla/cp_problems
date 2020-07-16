# isRotated(str1, str2) [10 pts]
# Write an efficient program to test if two given String is a rotation of each other or not, e.g.
# if given String is "XYZ" and "ZXY" then your function should return true, but if the input is
# "XYZ" and "YXZ" then return false.


def isrotated(str1, str2):
    # Your code goes here
    for i in range(len(str1) - 1, 0, -1):
        return str2 == str1[i:] + str1[:i] or str1 == str2[i:] + str2[:i]
