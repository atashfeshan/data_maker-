import turtle as t
import numpy as np

def draw(x, ball):
    t.clear()
    t.speed('fastest')
    t.penup()
    t.goto(7 * 50, 4 * 50)
    t.pendown()
    t.goto(-7 * 50, 4 * 50)
    t.goto(-7 * 50, -4 * 50)
    t.goto(7 * 50, -4 * 50)
    t.goto(7 * 50, 4 * 50)
    t.goto(7 * 50, -1.4 * 50)
    t.dot(10)
    t.goto(7 * 50, 1.4 * 50)
    t.dot(10)
    t.penup()
    t.goto(-7 * 50, -1.4 * 50)
    t.dot(10)
    t.goto(-7 * 50, 1.4 * 50)
    t.dot(10)
    t.goto(ball[0]*50, ball[1]*50)
    t.dot(25)
    for j,i in enumerate(x):
        if j > 4:
            t.color('red', 'red')
        else:
            t.color('black', 'black')
        t.goto(i[0]*50, i[1]*50)
        t.write(j+1)
        t.pendown()
        t.circle(25)
        t.penup()


