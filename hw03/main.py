import turtle as t
t.hideturtle()
t.penup()
t.goto(-576,384)
t.pendown()
t.color('red','red')
t.begin_fill()
for i in range(1):
    t.forward(900)
    t.right(90)
    t.forward(600)
    t.right(90)
    t.forward(900)
    t.right(90)
    t.forward(600)
t.end_fill()
t.penup()
#第一颗星
t.goto(-426,324)
t.pendown()
t.right(162)
t.color('yellow','yellow')
t.begin_fill()
for i in range(5):
    t.forward(171)
    t.right(144)
t.end_fill()
#第二颗星
t.penup()
t.goto(-301,309)
t.pendown()
t.right(240)
t.begin_fill()
for i in range(5):
    t.forward(58)
    t.right(144)
t.end_fill()
#第三颗星
t.penup()
t.goto(-246,263)
t.pendown()
t.right(20)
t.begin_fill()
for i in range(5):
    t.forward(58)
    t.right(144)

t.end_fill()
#第四颗星
t.penup()
t.goto(-241,179)
t.pendown()
t.right(25)
t.begin_fill()
for i in range(5):
    t.forward(58)
    t.right(144)
t.end_fill()
#第五颗星
t.penup()
t.goto(-291,124)
t.pendown()
t.right(25)
t.begin_fill()
for i in range(5):
    t.forward(58)
    t.right(144)
t.end_fill()
