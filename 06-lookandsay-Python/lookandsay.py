# First, you can read about look-and-say numbers here. Then, write the function lookAndSay(a) that takes a list of
# numbers and returns a list of numbers that results from "reading off" the initial list using the look-and-say
# method, using tuples for each (count, value) pair. For example:
# lookAndSay([]) == []
# lookAndSay([1,1,1]) == [(3,1)]
# lookAndSay([-1,2,7]) == [(1,-1),(1,2),(1,7)]
# lookAndSay([3,3,8,-10,-10,-10]) == [(2,3),(1,8),(3,-10)]
# lookAndSay([3,3,8,3,3,3,3]) == [(2,3),(1,8),(4,3)]

def lookandsay(a):
    # Your code goes here
    l = []
    i = 0
    while i < len(a):
        if i == len(a) - 1:
            l.append((1, a[-1]))
            return l
        count = 1
        while a[i] == a[i + 1]:
            count += 1
            i += 1
            if i + 1 == len(a):
                break
        l.append((count, a[i]))
        i += 1
    return l


# print(lookandsay([-1, 2, 7, 7]))
