import turtle,time
turtle.bgcolor('red')
turtle.tracer(2)
t1 = turtle.Turtle('turtle')
t2 = turtle.Turtle('turtle')

def multiple(turtle,clr,size):
  turtle.color(clr)
  turtle.shapesize(size)
  turtle.pensize(4)
  turtle.left(90)
  turtle.speed(10)
  
multiple(t1,'blue',2)
multiple(t2,'gold',1)

X=10
for s in range (20):
  t1.up()
  t2.up()
  t1.goto(-200+10*s,200-20*s)
  t2.goto(-200+10*s,200-20*s)
  t1.down()
  t2.down()
  for i in range (36):
    t1.forward(X)
    t1.left(10)
    t2.forward(X)
    t2.right(10)
t1.hideturtle()
t2.hideturtle()

