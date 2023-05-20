import turtle

mt = turtle.Turtle()
mt.pu()
mt.goto(-200, 0)
mt.pd()

x = 10 # length
iter = 4 # iterations
angle = 60 # the angle at da tippy top

def regKoch(val: int):
    if val == 0:
        return
    
    regKoch(val-1)
    mt.lt(90-(angle/2))
    mt.fd(x)
    regKoch(val-1)
    mt.rt(180-angle)
    mt.fd(x)
    regKoch(val-1)
    mt.lt(90-(angle/2))
    mt.fd(x)
    regKoch(val-1)

# mt.fd(x)
# regKoch(iter)


def skewKoch(val: int):
    if val == 0:
        return
    
    skewKoch(val-1)
    mt.lt(90-(angle/2))
    mt.fd(x)
    skewKoch(val-1)
    mt.rt(180-angle)
    mt.fd(x)
    skewKoch(val-1)
    mt.lt(90-(angle/2))
    mt.fd(x/2)
    skewKoch(val-1)

mt.fd(x)
skewKoch(iter)


# koch w same (triangle) base, that gets extended to be pointier => will intersect





screen = turtle.Screen()
screen.mainloop()