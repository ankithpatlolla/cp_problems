# canQueenAttack(qX, qY, oX, oY) [15 pts]
# Given the position of the queen (qX, qY) and the opponent (oX, oY) on a chessboard. The task is to determine
# whether the queen can attack the opponent or not. Note that the queen can attack in the same row, same column and
# diagonally.


def diff(x, y):
    return abs(x - y)


def canqueenattack(qR, qC, oR, oC):
    # Your code goes here
    if diff(qR, oR) == diff(qC, oC) or (diff(qR, oR) == 1 and qC == oC) or (diff(qC, oC) == 1 and qR == oR):
        return True
    return False
