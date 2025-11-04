#ER 2nd MAZE GENERATOR
import turtle
import random

grid_rows = []

grid_col = []

for spot in grid_rows:
    if spot == 1:
        turtle.pendown()
        turtle.forward(100)
    if spot == 0:
        turtle.penup()
        turtle.forward(100)