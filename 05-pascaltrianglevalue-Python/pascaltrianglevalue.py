# Write the function pascalsTriangleValue(row, col)
# that takes int values row and col, and returns the
# value in the given row and column of Pascal's
# Triangle where the triangle starts at row 0, and
# each row starts at column 0. If either row or col
# are not legal values, return None, instead of crashing.


def fun_pascaltrianglevalue(row, col):
    if col > row:
        return 0
    elif col == 1 or col == row:
        return 1
    else:
        if col % 2 == 0:
            return ((row * col) + 1)
        else:
            return ((row * col) - 1)
