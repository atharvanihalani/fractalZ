import turtle

mt = turtle.Turtle()
mt.hideturtle()
mt.speed(0)
mt.pu()
mt.goto(-350, 0)
mt.pd()


def reg_koch_1(iter: int, len: float, angle: float):
    '''
    initialize wiith start length \r\n
    angle is constant height w varying base size
    '''

    if iter == 0:
        return
    
    reg_koch_1(iter-1, len, angle)
    mt.lt(90-(angle/2))
    mt.fd(len)
    reg_koch_1(iter-1, len, angle)
    mt.rt(180-angle)
    mt.fd(len)
    reg_koch_1(iter-1, len, angle)
    mt.lt(90-(angle/2))
    mt.fd(len)
    reg_koch_1(iter-1, len, angle)

def reg_koch_2(iter: int, len: int, angle: float):
    '''
    iter index is 'forward shifted' compared to the prev method \r\n
    again, angle is constant length w varying base size
    '''
    reg_koch_2_helper(iter, len, angle)
    mt.lt(90-(angle/2))
    reg_koch_2_helper(iter, len, angle)
    mt.rt(180-angle)
    reg_koch_2_helper(iter, len, angle)
    mt.lt(90-(angle/2))
    reg_koch_2_helper(iter, len, angle)

def reg_koch_2_helper(iter: int, len: float, angle: float):
    if iter == 0:
        mt.fd(len)
    else:
        reg_koch_2(iter-1, len, angle)

# 'skews' the curve at the lowest recursive level
def faux_koch_1(iter: int, len: int, angle: float):
    if iter == 0:
        return
    
    faux_koch_1(iter-1, len, 60)
    mt.fd(len)
    mt.lt(90-(angle/2))
    faux_koch_1(iter-1, len, 60)
    mt.fd(len)
    mt.rt(180-angle)
    faux_koch_1(iter-1, len, 60)
    mt.fd(len)
    mt.lt(90-(angle/2))
    faux_koch_1(iter-1, len, 60)
    mt.fd(len)

# koch curve but skewed (and hence, scaled slightly diff)
def skew_koch(iter: int, len: float, angle: float):
    '''
    initialize w start length x
    '''

    if iter == 0:
        return
    
    skew_koch(iter-1, len, angle)
    mt.lt(90-(angle/2))
    mt.fd(len/2)
    skew_koch(iter-1, len/2, angle)
    mt.rt(180-angle)
    mt.fd(len/2)
    skew_koch(iter-1, len/2, angle)
    mt.lt(90-(angle/2))
    mt.fd(len/2)
    skew_koch(iter-1, len/2, angle)

mt.fd(50)
skew_koch(3, 50, 60)


# koch w same (triangle) base, that gets extended to be pointier => will intersect
# infinitely generating koch curve (unbounded recursion)
# defined area (rather than defined side length) => pass x/2 as recursive param



screen = turtle.Screen()
screen.mainloop()