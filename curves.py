import turtle
from enum import Enum

mt = turtle.Turtle()
mt.hideturtle()
mt.speed(0)
mt.pu()
mt.goto(-200, 200)
mt.pd()

def gosper_island(iter: int, size: float, angle: float = 60):
    '''
    "top level function"; it joins each segment together into a hexagon
    iter: how many iterations 'deep' the graphic should go
    size: the, ummm, size
    angle: default for the gosper island is 60; you can tweak it tho
    '''
    for _ in range(6):
        gosper_segment(iter, size, angle)
        mt.lt(60)

def gosper_segment(iter: int, len: float, angle: float):
    '''
    recursively generates a single segment of the gosper curve (hexagon)'''
    gosper_segment_helper(iter, len, angle)
    mt.rt(angle)
    gosper_segment_helper(iter, len, angle)
    mt.lt(angle)
    gosper_segment_helper(iter, len, angle)

def gosper_segment_helper(iter: int, len: float, angle: float):
    '''
    helper method for generating a gosper segment'''
    if iter == 0:
        mt.fd(len)
    else:
        gosper_segment(iter-1, len/2.5, angle)


# the following code generates three different variants of a quadric koch island
# a lot of code is shared (specifically, the top-level and the helper methods), 
# so I've parametrized the variants with the Islands enum
class Islands(Enum):
    '''
    Enum representing three different koch curves with increasing complexity'''
    SIMPLE = 0
    COMPLEX = 1
    UNHINGED = 2

def koch_island(island: Islands, iter: int, size: float, angle: float, is_square: bool):
    '''
    this is the common top-level method for generating the three 
    quadric koch variants. each variant has a different method 
    for generating a particular segment. this method loops over 
    the submethods & pieces them together as one polygon\r\n
    hoo boy, that's a lot of params. let's go over em tog \n
    island: the enum selecting which curve is generated
    iter: how many iterations deep should we go
    size: well, the size
    angle: the angle of each 'bend'
    is_square: this is a fun little flag. if true, the fractal 
    initiator is your classic square. else, the initiator is the 
    closest (regular) polygon whose internal angle = angle
    '''
    # determines the num of sides & the angle of the polygon
    island_sides = 4 if is_square else round(360/angle)
    turn_by = 90 if is_square else 360/island_sides
    
    # 'switch' statement to decide which submethod to call
    body_func = None
    match island:
        case Islands.SIMPLE:
            body_func = koch_seg_simple
        case Islands.COMPLEX:
            body_func = koch_seg_complex
        case Islands.UNHINGED:
            body_func = koch_seg_unhinged
        case _:
            print("ur mom")
            body_func = koch_seg_simple

    # loops over & pieces the individual sides (ie. curves) together
    for _ in range(island_sides):
        body_func(iter, size, angle)
        mt.rt(turn_by)

def koch_seg_simple(iter: int, len: float, angle: float):
    '''
    recursive method to generate a simple quadric koch curve'''
    koch_seg_helper(iter, len/4, angle, koch_seg_simple)
    mt.lt(angle)
    koch_seg_helper(iter, len/4, angle, koch_seg_simple)
    mt.rt(angle)
    koch_seg_helper(iter, len/4, angle, koch_seg_simple)
    mt.rt(angle)
    koch_seg_helper(iter, len/4, angle, koch_seg_simple)
    koch_seg_helper(iter, len/4, angle, koch_seg_simple)
    mt.lt(angle)
    koch_seg_helper(iter, len/4, angle, koch_seg_simple)
    mt.lt(angle)
    koch_seg_helper(iter, len/4, angle, koch_seg_simple)
    mt.rt(angle)
    koch_seg_helper(iter, len/4, angle, koch_seg_simple)
    pass

def koch_seg_complex(iter: int, len: float, angle: float):
    '''
    recursive method to generate a complex quadric koch curve'''
    koch_seg_helper(iter, len/6, angle, koch_seg_complex)
    mt.lt(90)
    koch_seg_helper(iter, len/6, angle, koch_seg_complex)
    koch_seg_helper(iter, len/6, angle, koch_seg_complex)
    mt.rt(90)
    koch_seg_helper(iter, len/6, angle, koch_seg_complex)
    koch_seg_helper(iter, len/6, angle, koch_seg_complex)
    mt.rt(90)
    koch_seg_helper(iter, len/6, angle, koch_seg_complex)
    mt.rt(90)
    koch_seg_helper(iter, len/6, angle, koch_seg_complex)
    mt.lt(90)
    koch_seg_helper(iter, len/6, angle, koch_seg_complex)
    mt.lt(90)
    koch_seg_helper(iter, len/6, angle, koch_seg_complex)
    koch_seg_helper(iter, len/6, angle, koch_seg_complex)
    mt.rt(90)
    koch_seg_helper(iter, len/6, angle, koch_seg_complex)
    mt.rt(90)
    koch_seg_helper(iter, len/6, angle, koch_seg_complex)
    mt.lt(90)
    koch_seg_helper(iter, len/6, angle, koch_seg_complex)
    mt.lt(90)
    koch_seg_helper(iter, len/6, angle, koch_seg_complex)
    koch_seg_helper(iter, len/6, angle, koch_seg_complex)
    mt.lt(90)
    koch_seg_helper(iter, len/6, angle, koch_seg_complex)
    koch_seg_helper(iter, len/6, angle, koch_seg_complex)
    mt.rt(90)
    koch_seg_helper(iter, len/6, angle, koch_seg_complex)

def koch_seg_unhinged(iter: int, len: float, angle: float):
    '''
    recursive method to generate an absolutely deranged quadric koch curve'''
    koch_seg_helper(iter, len/8, angle, koch_seg_unhinged)
    mt.rt(90)
    koch_seg_helper(iter, len/8, angle, koch_seg_unhinged)
    mt.lt(90)
    koch_seg_helper(iter, len/8, angle, koch_seg_unhinged)
    mt.lt(90)
    koch_seg_helper(iter, len/8, angle, koch_seg_unhinged)
    mt.rt(90)
    koch_seg_helper(iter, len/8, angle, koch_seg_unhinged)
    mt.rt(90)
    koch_seg_helper(iter, len/8, angle, koch_seg_unhinged)
    koch_seg_helper(iter, len/8, angle, koch_seg_unhinged)
    mt.lt(90)
    koch_seg_helper(iter, len/8, angle, koch_seg_unhinged)
    mt.rt(90)
    koch_seg_helper(iter, len/8, angle, koch_seg_unhinged)
    mt.rt(90)
    koch_seg_helper(iter, len/8, angle, koch_seg_unhinged)
    koch_seg_helper(iter, len/8, angle, koch_seg_unhinged)
    mt.lt(90)
    koch_seg_helper(iter, len/8, angle, koch_seg_unhinged)
    mt.lt(90)
    koch_seg_helper(iter, len/8, angle, koch_seg_unhinged)
    mt.lt(90)
    koch_seg_helper(iter, len/8, angle, koch_seg_unhinged)
    koch_seg_helper(iter, len/8, angle, koch_seg_unhinged)
    mt.rt(90)
    koch_seg_helper(iter, len/8, angle, koch_seg_unhinged)
    koch_seg_helper(iter, len/8, angle, koch_seg_unhinged)
    mt.lt(90)
    koch_seg_helper(iter, len/8, angle, koch_seg_unhinged)
    koch_seg_helper(iter, len/8, angle, koch_seg_unhinged)
    mt.rt(90)
    koch_seg_helper(iter, len/8, angle, koch_seg_unhinged)
    mt.rt(90)
    koch_seg_helper(iter, len/8, angle, koch_seg_unhinged)
    mt.lt(90)
    koch_seg_helper(iter, len/8, angle, koch_seg_unhinged)
    koch_seg_helper(iter, len/8, angle, koch_seg_unhinged)
    mt.lt(90)
    koch_seg_helper(iter, len/8, angle, koch_seg_unhinged)
    mt.lt(90)
    koch_seg_helper(iter, len/8, angle, koch_seg_unhinged)
    mt.rt(90)
    koch_seg_helper(iter, len/8, angle, koch_seg_unhinged)
    koch_seg_helper(iter, len/8, angle, koch_seg_unhinged)
    mt.lt(90)
    koch_seg_helper(iter, len/8, angle, koch_seg_unhinged)
    mt.lt(90)
    koch_seg_helper(iter, len/8, angle, koch_seg_unhinged)
    mt.rt(90)
    koch_seg_helper(iter, len/8, angle, koch_seg_unhinged)
    mt.rt(90)
    koch_seg_helper(iter, len/8, angle, koch_seg_unhinged)
    mt.lt(90)
    koch_seg_helper(iter, len/8, angle, koch_seg_unhinged)

def koch_seg_helper(iter: int, len: float, angle: float, recurse_to):
    '''
    common helper method for all koch curve generators'''
    if iter == 0:
        mt.fd(len)
    else:
        recurse_to(iter-1, len, angle)

# EXAMPLE CALLS
# koch_island(Islands.COMPLEX, 2, 400, 90, True)


screen = turtle.Screen()
screen.mainloop()