from turtle import *

def drawKoch(n):
    '''draws nth Koch curve using instructions from function koch()'''
    s = Screen()              # create screen
    t = Turtle()              # create turtle    
    directions = koch(n)      # obtain directions to draw Koch(n)
    for move in directions:   # follow the specified moves
        if move == 'F':
            t.forward(300/3**n)   # forward move length, normalized 
        if move == 'L':
            t.lt(60)              # rotate left 60 degrees
        if move == 'R':
            t.rt(120)             # rotate right 60 degrees
    s.bye()
def koch(n):
    'returns directions for drawing curve Koch(n)'
    if n==0:
        return 'F'
    # recursive step: get directions for Koch(n-1)
    tmp = koch(n-1)
    # use them to construct directions for Koch(n)
    return tmp+'L'+tmp+'R'+tmp+'L'+tmp

drawKoch(3)
