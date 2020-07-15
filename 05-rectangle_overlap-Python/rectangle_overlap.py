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

    lt1 = [left1, top1]
    rt1 = [right1, top1]
    bl1 = [left1, bottom1]
    br1 = [right1, bottom1]

    lt2 = [left2, top2]
    rt2 = [right2, top2]
    bl2 = [left2, bottom2]
    br2 = [right2, bottom2]

    if (rt1[1] <= bl2[1]) or (bl1[1] >= rt2[1]) or (rt1[0] <= bl2[0]) or (bl1[0] >= rt2[0]):
        return False

    if (lt1[0] > br2[0]) or (lt2[0] > br1[0]) or (lt1[1] > br2[1]) or (lt2[1] < br1[1]):
        return False
    return True
