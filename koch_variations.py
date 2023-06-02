import turtle

mt = turtle.Turtle()
mt.hideturtle()
mt.speed(0)
mt.pu()
mt.goto(-200, 0)
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
    again, angle is constant length w varying base size \r\n
    just a different way to write the same function    
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


def reg_koch_3(iter: int, size: float, angle: float):
    '''
    same thing as before w a teeny-tiny difference
    here, the TOTAL size/area of the curve remains constant &
    the length of each segment is inversely proportional to iter
    '''
    reg_koch_3_helper(iter, size/3, angle)
    mt.lt(90-(angle/2))
    reg_koch_3_helper(iter, size/3, angle)
    mt.rt(180-angle)
    reg_koch_3_helper(iter, size/3, angle)
    mt.lt(90-(angle/2))
    reg_koch_3_helper(iter, size/3, angle)

def reg_koch_3_helper(iter: int, size: float, angle: float):
    if iter == 0:
        mt.fd(size)
    else:
        reg_koch_3(iter-1, size, angle)


def infinite_koch(len: int, angle: float):
    '''
    or in other words: how to make ur computer run out of ram \r\n
    does what it says; creates an ever-expanding koch curve \r\n
    took me a HOT sec to figure out the nub for all its apparent simplicity
    '''
    
    mt.screen.setworldcoordinates(-20, -20, 15*len, 15*len)
    mt.fd(len)
    i = 0

    while i >= 0:
        mt.hideturtle()
        mt.speed(0)
        inf_koch_helperA(i, len, angle, True)
        i += 1
        mt.screen.setworldcoordinates(-20, -20, 3*len*(3**i), 3*len*(3**i))

def inf_koch_helperA(iter: int, len: int, angle: float, to_skip: bool):
    '''
    this method is almost identical to reg_koch_2 and its 
    helper counterpart \r\n
    the only difference is the inclusion of the to_skip flag.
    this ensures that the first 'quarter' of the curve is skipped'''

    if (to_skip):
        pass
    else:
        inf_koch_helperB(iter, len, angle)
    mt.lt(90-(angle/2))
    inf_koch_helperB(iter, len, angle)
    mt.rt(180-angle)
    inf_koch_helperB(iter, len, angle)
    mt.lt(90-(angle/2))
    inf_koch_helperB(iter, len, angle)

def inf_koch_helperB(iter: int, len: float, angle: float):
    if iter == 0:
        mt.fd(len)
    else:
        inf_koch_helperA(iter-1, len, angle, False)


def faux_koch_1(iter: int, len: int, angle: float):
    '''
    'skews' the curve, but only at the lowest recursive level
    '''
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


def skew_koch(iter: int, len: float, angle: float):
    '''
    initialize w start length x
    skews the entire koch curve (& also scalees it slightly diff)
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


def koch_triangle(iter: int, len: int, angle: float):
    reg_koch_2(iter, len, angle)
    mt.rt(120)
    reg_koch_2(iter, len, angle)
    mt.rt(120)
    reg_koch_2(iter, len, angle)


screen = turtle.Screen()
screen.mainloop()