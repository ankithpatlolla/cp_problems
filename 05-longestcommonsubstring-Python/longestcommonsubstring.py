# longestCommonSubstring(s1, s2)[20 pts]
# Write the function, longestCommonSubstring(s1, s2), that takes two possibly-empty strings and returns the longest
# string that occurs in both strings (and returns the empty string if either string is empty). For example:
# longestCommonSubstring("abcdef", "abqrcdest") returns "cde"
# longestCommonSubstring("abcdef", "ghi") returns "" (the empty string)
# If there are two or more longest common substrings, return the lexicographically smaller one (ie, just use "<" to
# compare the strings). So, for example:
# longestCommonSubstring("abcABC", "zzabZZAB") returns "AB" and not "ab"

def longestcommonsubstring(s1, s2):
    # Yourcode goes here
    res = ""
    prev = ""
    l = []
    if len(s1) == 0 or len(s2) == 0:
        return ""
    if len(s1) > len(s2):
        s1, s2 = s2, s1
    for i in range(len(s1)):
        s = ""
        for j in range(i, len(s1)):
            s += s1[j]
            # print(s, "ssssssssssss")
            if s in s2:
                if len(res) <= len(s):
                    res = s
                    res = min(s, res)
    return res


print(longestcommonsubstring("abcxyz", "xyzabtgfjabc"))
