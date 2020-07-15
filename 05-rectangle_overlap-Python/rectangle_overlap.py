# rectanglesOverlap(left1, top1, width1, height1, left2, top2, width2, height2)
# A rectangle can be described by its left, top, width, and height. This function
# takes two rectangles described this way, and returns True if the rectangles
# overlap at all (even if just at a point), and False otherwise.
# Note: here we will represent coordinates the way they are usually represented in
# computer graphics, where (0,0) is at the left-top corner of the screen, and while
# the x-coordinate goes up while you head right, the y-coordinate goes up while you
# head down (so we say that "up is down")

def fun_rectangle_overlap(left1, top1, width1, height1, left2, top2, width2, height2):
    right1 = left1 + width1
    bottom1 = top1 + height1
    right2 = left2 + width2
    bottom2 = top2 + height2

    ltl1 = [left1, top1]
    ltr1 = [right1, top1]
    btl1 = [left1, bottom1]
    btr1 = [right1, bottom1]

    ltl2 = [left2, top2]
    ltr2 = [right2, top2]
    btl2 = [left2, bottom2]
    btr2 = [right2, bottom2]

    if (ltl1[0] >= btr2[0]) or (ltl2[0] >= btr1[0]):
        return False
    if (ltl1[1] <= btr2[1]) or (ltl2[1] <= btr1[1]):
        return False
    return True
