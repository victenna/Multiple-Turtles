import turtle
import time
t=turtle.Turtle()
wn=turtle.Screen()
wn.bgcolor('dark blue')
turtle.tracer(3)
t.color('coral')
t1=turtle.Turtle()
t2=turtle.Turtle()
t3=turtle.Turtle()
t1.color('gray')
t2.color('gray')

t3.hideturtle()

t.penup()
t1.penup()
t2.penup()

t.shape('square')
t1.shape('circle')
t2.shape('circle')

t.turtlesize(4,12)
t1.turtlesize(2)
t2.turtlesize(2)

t3.up()
t3.goto(-460,-95)
t3.down()
t3.color('green')
t3.begin_fill()
for j in range (2):
    t3.fd(900)
    t3.left(90)
    t3.fd(15)
    t3.left(90)
t3.end_fill()
i=-1
while True:
    i=i+1
    t.goto(-400+5*i,0)
    t1.goto(-460+5*i,-60)
    t2.goto(-340+5*i,-60)
    time.sleep(0.02)
    if t.xcor()>350:
        i=-1
        






