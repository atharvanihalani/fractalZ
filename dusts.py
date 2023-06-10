import turtle
from typing import List
import math

mt = turtle.Turtle()
mt.hideturtle()
mt.speed(0)

def og_dust_stack(length: float, limit: int):
    '''
    creates a stack of cantor dust 'bars' up to 
     the specified iteration count. \n
    length: size of the entire 'bar' 
    limit: how many iterations to 'stack' '''    
    for i in range(limit):
        mt.pu()
        mt.goto(-length/2, -i*40)
        mt.pd()
        og_dust(length, i)

def og_dust(length: float, iter: int):
    '''
    creates your classic cantor dust \n
    length: size of the entire 'bar' 
    iter: how many iterations deep is the dust '''
    if iter == 0:
        mt.fd(length)
        return
        
    og_dust(length/3, iter-1)
    mt.pu()
    mt.fd(length/3)
    mt.pd()
    og_dust(length/3, iter-1)


def parametrized_stack(length: float, limit: int, curds: int, c_t_ratio: float):
    '''
    stacks increasing iterations of parametrized fractal dust \n
    length: size of the entire bar
    limit: how many iterations to 'stack'
    curds: ie. how many fragments does each bar 
           break up into
    c_t_ratio: constant curd-to-trema ratio; ie the
               ratio between a fragment and a gap'''
    for i in range(limit):
        mt.pu()
        mt.goto(-length/2, -i*40)
        mt.pd()
        parametrized_dust(length, i, curds, c_t_ratio)

def parametrized_dust(length: float, iter: int, curds: int, c_t_ratio: float):
    '''
    a more parametrized version of fractal dust (but
    still not FULLY there) \n
    length: size of the entire bar
    iter: how many iterations deep is the dust
    curds: ie. how many fragments does each bar 
           break up into
    c_t_ratio: constant curd-to-trema ratio; ie the
               ratio between a fragment and a gap'''
    if iter == 0:
        mt.fd(length)
        return
    
    c_len = (length*c_t_ratio)/(curds*c_t_ratio + curds - 1)
    t_len = c_len/c_t_ratio

    for i in range(curds-1):
        parametrized_dust(c_len, iter-1, curds, c_t_ratio)
        mt.pu()
        mt.fd(t_len)
        mt.pd()
    parametrized_dust(c_len, iter-1, curds, c_t_ratio)    


def cyoa_stack(length: float, limit: int, generator: List[float]):
    '''
    stacks up the cyoa dust!!
    length: size of the entire bar
    iter: how many iterations deep is the dust
    generator: specify the fractal generator yourself!
               eg. [1, 3, 2, 3, 1] would have 3 'curds' 
               of respective proportions 1, 2, and 1. 
               they'd each be separated by gaps of size 3    '''
    for i in range(limit):
        mt.pu()
        mt.goto(-length/2, -i*40)
        mt.pd()
        cyoa_dust(length, i, generator, sum(generator))

def cyoa_dust(length: float, iter: int, generator: List[float], sum):
    '''
    create you own fractal dust!
    wholesome fun for the entire family!! \n
    length: size of the entire bar
    iter: how many iterations deep is the dust
    generator: specify the fractal generator yourself!
               eg. [1, 3, 2, 3, 1] would have 3 'curds' 
               of respective proportions 1, 2, and 1. 
               they'd each be separated by gaps of size 3
    sum: sum(generator) - so you don't have to recalculate
         it on every iteration'''

    if iter == 0:
        mt.fd(length)
        return

    for i in range(math.floor(len(generator)/2)):
        new_len = (length*generator[2*i])/sum
        new_gap = (length*generator[2*i+1])/sum
        cyoa_dust(new_len, iter-1, generator, sum)
        mt.pu()
        mt.fd(new_gap)
        mt.pd()
        pass

    if len(generator) % 2:
        new_len = (length*generator[len(generator)-1])/sum
        cyoa_dust(new_len, iter-1, generator, sum)


# EXAMPLE CALLS:
# og_dust_stack(200, 3)
# 
# parametrized_dust(200, 4, 3, 0.5)
# 
# cyoa_stack(300, 8, [1, 2, 3, 2, 1])



screen = turtle.Screen()
screen.mainloop()