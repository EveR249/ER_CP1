#ER 2nd Turtle race
import turtle
import random

#moving function
def race():
        pink.forward(random.randint(10,40))
        purple.forward(random.randint(10,40))
        yellow.forward(random.randint(10,40))
        green.forward(random.randint(10,40))
        blue.forward(random.randint(10,40))

#create finish line
def finish():
    turtle.hideturtle()
    turtle.pensize(20)
    turtle.penup()
    turtle.setx(400)
    turtle.pendown()
    turtle.sety(500)
    turtle.sety(-500)

#set turtles
def create(turt_name):
     turt_name.shape("turtle")
     turt_name.shapesize(3)
     turt_name.pensize(5)
     turt_name.penup()


#Set pink turtle
pink = turtle.Turtle()
create(pink)
pink.color("pink")
#Go to start
pink.goto(-700,400)
pink.pendown()

#Set purple turtle
purple = turtle.Turtle()
create(purple)
purple.color("purple")
#Go to start
purple.goto(-700,200)
purple.pendown()

#Set yellow turtle
yellow = turtle.Turtle()
create(yellow)
yellow.color("yellow")
#Go to start
yellow.goto(-700,0)
yellow.pendown()

#Set green turtle
green = turtle.Turtle()
create(green)
green.color("green")
#Go to start
green.goto(-700,-200)
green.pendown()

#Set blue turtle
blue = turtle.Turtle()
create(blue)
blue.color("blue")
#Go to start
blue.goto(-700,-400)
blue.pendown()

#put in loop and check win
while True:
    turtle.onclick(finish())
    turtle.onclick(race())
    if pink.xcor() >= 400:
        print("Pink Won!")
        break
    if purple.xcor() >= 400:
        print("Purple Won!")
        break
    if yellow.xcor() >= 400:
        print("Yellow Won!")
        break
    if green.xcor() >= 400:
        print("Green Won!")
        break
    if blue.xcor() >= 400:
        print("Blue Won!")
        break

turtle.done()
