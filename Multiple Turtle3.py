import turtle,time
turtle.bgcolor('darksalmon')
wn=turtle.Screen()
turtle.tracer(4)
q=[]
clr=['pink','blue','gold','red','green']
pos=[(0,0),(150,150),(-150,150),(-150,-150),(150,-150)]

for n in range (5):
    q.append(turtle.Turtle())
    q[n].shape('turtle')
    q[n].shapesize(5)
    q[n].color(clr[n])
    q[n].up()
    q[n].goto(pos[n])
def mov():
    for i in range(5):
        q[i].left(1)
while True:
    mov()
    

