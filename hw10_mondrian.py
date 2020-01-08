# ----------------------------------------------------------
# --------              HW 10: Recursive mondrian art ------
# ----------------------------------------------------------

# ----------------------------------------------------------
# Name: Mia McDuffie
# Time spent on this assignment: 7 hr
#
# Collaborators and sources:
#   https://docs.python.org/2/library/turtle.html#turtle.fillcolor
#
#
# ----------------------------------------------------------

import turtle
from random import randint, random


WIDTH = 1024
HEIGHT = 768

SPLIT_LOW = 120
SPLIT_PENALTY = 1.5

def randomColor():
    #returns a random RGB color
     rv = random()
     if rv < 0.0833:
       return "red"
     elif rv < 0.1667:
       return "skyblue"
     elif rv < 0.25:
       return "yellow"
     else:
       return "white"


def drawRectangle(x1, y1, x2, y2, t):
    #Draws a random rectangle with the given corner ponints using a random color
    color = randomColor()
    #pencolor(red, greem, blue)
    t.fillcolor(color)
    t.begin_fill()
    t.up()
    t.goto(x1, y1)
    t.down()
    t.goto(x2, y1)
    t.goto(x2, y2)
    t.goto(x1, y2)
    t.goto(x1, y1)
    t.end_fill()

def mondrian(x1, y1, x2, y2, level, t):
    #Draws a Mondrian-like painting at the given level
    if level > 0:                       #base case
        drawRectangle(x1, y1, x2, y2, t)
        vertical = randint(1, 2)
        splitFactor = randint(1, 2)
        if vertical == 1:               #Vertical split
            if splitFactor == 1:        #Do 1/3 and 2/3
                mondrian(x1, y1, (x2 - x1) / 3 + x1, y2, level - 1, t)
                mondrian((x2 - x1) / 3 + x1, y1, x2, y2, level - 1, t)
            else:                       #Do 2/3 and 1/3
                mondrian(x1, y1, 2 * (x2 - x1) / 3 + x1, y2, level - 1, t)
                mondrian(2 * (x2 - x1) / 3 + x1, y1, x2, y2, level - 1, t)
        elif splitFactor == 1:          #Horizontal split with 1/3 and 2/3
            mondrian(x1, y1, x2, y1 - (y1 - y2) / 3, level - 1, t)
            mondrian(x1, y1, x2, y1 - (y1 - y2) / 3, level - 1, t)
        else:
            mondrian(x1, y1, x2, y1 - 2 * (y1 - y2) / 3, level - 1, t)
            mondrian(x1, y1 - 2 * (y1 - y2) / 3, x2, y2, level - 1, t)

def main():
    # Create a window with a t
    wn = turtle.Screen()
    wn.setworldcoordinates(0, 0, WIDTH+1, HEIGHT+1)
    t = turtle.Turtle()
    t.pensize(5)
    t.speed(0)
    t.hideturtle()

    # Draw the art
    level = randint(3, 7)
    print(level)
    mondrian(0, 0, WIDTH, HEIGHT, level, t)
    wn.exitonclick()

if __name__ == '__main__':
    main()
