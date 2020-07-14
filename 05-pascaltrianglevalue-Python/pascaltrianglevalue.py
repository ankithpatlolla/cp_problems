# Write the function pascalsTriangleValue(row, col)
# that takes int values row and col, and returns the
# value in the given row and column of Pascal's
# Triangle where the triangle starts at row 0, and
# each row starts at column 0. If either row or col
# are not legal values, return None, instead of crashing.

def fac(n):
    if n == 0:
        return 1
    return n * fac(n - 1)


def fun_pascaltrianglevalue(row, col):
    if col > row:
        return 0
    elif col == 0 or col == row:
        return 1
    else:
        return (fac(row) / (fac(row - col) * fac(col)))
