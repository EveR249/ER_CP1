#ER 2nd Turtle race
import turtle
import random
def race():
    for x in range (50):
        pink.forward(random.randint(10,40))
        purple.forward(random.randint(10,40))
        yellow.forward(random.randint(10,40))
        green.forward(random.randint(10,40))
        blue.forward(random.randint(10,40))

#create finish line
turtle.hideturtle()
turtle.pensize(20)
turtle.penup()
turtle.setx(400)
turtle.pendown()
turtle.sety(500)
turtle.sety(-500)

#Set pink turtle
pink = turtle.Turtle()
pink.fillcolor("pink")
#set shape to turtle
pink.shape("turtle")
#set size to turtle
pink.shapesize(3)
#pen up
pink.penup()
#Go to start
pink.goto(-700,400)
pink.pendown()
pink.color("pink")
pink.pensize(5)

#set purple turtle
purple = turtle.Turtle()
purple.fillcolor ("purple")
#set shape to turtle
purple.shape("turtle")
#set size to turtle
purple.shapesize(3)
#pen up
purple.penup()
#Go to start
purple.goto(-700,200)
purple.pendown()
purple.color("purple")
purple.pensize(5)

#set yellow turtle
yellow = turtle.Turtle()
yellow.fillcolor ("yellow")
#set shape to turtle
yellow.shape("turtle")
#set size to turtle
yellow.shapesize(3)
#pen up
yellow.penup()
#Go to start
yellow.goto(-700,0)
yellow.pendown()
yellow.color("yellow")
yellow.pensize(5)

#set green turtle
green = turtle.Turtle()
green.fillcolor ("green")
#set shape to turtle
green.shape("turtle")
#set size to turtle
green.shapesize(3)
#pen up
green.penup()
#Go to start
green.goto(-700,-200)
green.pendown()
green.color("green")
green.pensize(5)

#set blue turtle
blue = turtle.Turtle()
blue.fillcolor ("blue")
#set shape to turtle
blue.shape("turtle")
#set size to turtle
blue.shapesize(3)
#pen up
blue.penup()
#Go to start
blue.goto(-700,-400)
blue.pendown()
blue.color("blue")
blue.pensize(5)


while True:
    turtle.onclick(race())
    turtle.done()
