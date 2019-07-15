import turtle,time,random
turtle.bgcolor('darksalmon')
wn=turtle.Screen()
turtle.tracer(3)
q=[]
clr=['pink','blue','gold','red','green','skyblue',\
     'hotpink','crimson','olive','tomato']

for n in range (len(clr)):
    t=turtle.Turtle('turtle')
    q.append(t)
    q[n].color(clr[n])
    q[n].down()
    angle=random.randint(-90,90)
    q[n].setheading(angle)
    
    
for j in range (15):
    for i in range(10):
        d=random.randint(20,30)
        angle=random.randint(-90,90)
        q[i].stamp()
        q[i].pensize(3)
        q[i].fd(d)
        q[i].left(angle)
        
    
    
            
    
