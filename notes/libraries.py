#ER 2nd Libraries notes
import random
import turtle
num = random.randint(100,500)

turtle.color("#1D6137")
turtle.pensize(20)
turtle.fillcolor("#73A888")
turtle.begin_fill()
for x in range(4):
    turtle.forward(250)
    turtle.right(90)
turtle.end_fill()

turtle.penup()
turtle.goto(-400,100)
turtle.shape("turtle")
turtle.shapesize(5)
turtle.pendown()
turtle.begin_fill()
for x in range(4):
    turtle.forward(250)
    turtle.right(90)
turtle.end_fill()

turtle.done()