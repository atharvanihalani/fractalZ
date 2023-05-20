import turtle

mt = turtle.Turtle()
mt.pu()
mt.goto(-350, 0)
mt.pd()

x = 3 # length
iter = 5 # iterations

def recKoch(val: int):
    if val == 0:
        return
    
    recKoch(val-1)
    mt.lt(60)
    mt.fd(x)
    recKoch(val-1)
    mt.rt(120)
    mt.fd(x)
    recKoch(val-1)
    mt.lt(60)
    mt.fd(x)
    recKoch(val-1)

mt.fd(x)
recKoch(iter)

screen = turtle.Screen()
screen.mainloop()