import turtle
import random

## 함수 선언 부분 ##dom


def screenLeftClick(x,y):
    tSize = random.randrange(2,10)
    turtle.shapesize(tSize)
    r = random.random()
    g = random.random()
    b = random.random()
    turtle.color((r, g, b))
    tAngle = random.randrange(0, 360)

    turtle.penup()
    turtle.goto(x,y)
    turtle.left(tAngle)
    turtle.stamp()

## 함수 선언 부분 ##

turtle.shape('turtle')
turtle.onscreenclick(screenLeftClick, 1)
turtle.done()
