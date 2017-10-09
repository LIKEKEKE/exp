import turtle as t

t.hideturtle()

def start(x,y,right,f):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.right(right)
    t.color('yellow','yellow')
    t.begin_fill()
    for i in range (5):
        t.forward(f)
        t.right(144)
    t.end_fill()
def rectangle(x,y,c,k):
    t.penup()
    t.goto(-575,384)
    t.pendown()
    t.color('red','red')
    t.begin_fill()
    for i in range(1):
        t.forward(c)
        t.right(90)
        t.forward(k)
        t.right(90)
        t.forward(c)
        t.right(90)
        t.forward(k)
    t.end_fill()
rectangle(-575,384,900,600)
start(-426,324,162,171)
start(-301,309,240,58)
start(-246,263,20,58)
start(-241,179,25,58)
start(-291,124,25,58)
