# sameChars(s1, s2) [20 pts]
# Write the function sameChars(s1, s2) that takes two strings and returns True if the two strings are composed of
# the same characters (though perhaps in different numbers and in different orders) -- that is, if every character
# that is in the first string, is in the second, and vice versa -- and False otherwise. This test is
# case-sensitive, so "ABC" and "abc" do not contain the same characters. The function returns False if either
# parameter is not a string, but returns True if both strings are empty (why?).

def samechars(s1, s2):
    # Your code goes here
    print(type(s1), type(s2))
    if type(s1) != 'str' and type(s2) != 'str':
        return False
    if len(s1) == 0 and len(s2) == 0:
        return True
    print(sorted(set(s1)), sorted(set(s2)))
    return sorted(set(s1)) == sorted(set(s2))


print(samechars("abcabcabc", "abc"))
