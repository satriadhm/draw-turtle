import turtle

t = turtle.Turtle()

x = 400

t.penup()
t.goto(0,x)

t.pendown()
for i in range(x):
    t.goto(-x,0)
    t.goto(0,-x)
    t.goto(x,0)
    t.goto(0,x)

    
t.done()

