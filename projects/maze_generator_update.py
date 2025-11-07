#ER 2nd Maze generator
import turtle
import random

#set variables
#Build functions
    #one function randomizes walls
    #one function checks if solvable
    #make sure you set start and stop correctly
    #Use path coordinates to check walls in each direction
#use turtle to draw the maze
#turtle moves the distance, you determines if pen is up or down
#need three functions

#set list of rows 6 "columns" inside each list, 6 lists inside a big list, each spot will be randomly assigned a 1 or a 0. same thing for columns

grid_row = [[[random.randint(0,1)],[random.randint(0,1)],[random.randint(0,1)],[random.randint(0,1)],[random.randint(0,1)],[random.randint(0,1)]],
            [[random.randint(0,1)],[random.randint(0,1)],[random.randint(0,1)],[random.randint(0,1)],[random.randint(0,1)],[random.randint(0,1)]],
            [[random.randint(0,1)],[random.randint(0,1)],[random.randint(0,1)],[random.randint(0,1)],[random.randint(0,1)],[random.randint(0,1)]],
            [[random.randint(0,1)],[random.randint(0,1)],[random.randint(0,1)],[random.randint(0,1)],[random.randint(0,1)],[random.randint(0,1)]],
            [[random.randint(0,1)],[random.randint(0,1)],[random.randint(0,1)],[random.randint(0,1)],[random.randint(0,1)],[random.randint(0,1)]]]

grid_col = [[[random.randint(0,1)],[random.randint(0,1)],[random.randint(0,1)],[random.randint(0,1)],[random.randint(0,1)],[random.randint(0,1)]],
            [[random.randint(0,1)],[random.randint(0,1)],[random.randint(0,1)],[random.randint(0,1)],[random.randint(0,1)],[random.randint(0,1)]],
            [[random.randint(0,1)],[random.randint(0,1)],[random.randint(0,1)],[random.randint(0,1)],[random.randint(0,1)],[random.randint(0,1)]],
            [[random.randint(0,1)],[random.randint(0,1)],[random.randint(0,1)],[random.randint(0,1)],[random.randint(0,1)],[random.randint(0,1)]],
            [[random.randint(0,1)],[random.randint(0,1)],[random.randint(0,1)],[random.randint(0,1)],[random.randint(0,1)],[random.randint(0,1)]]]
#Make a function to randomize walls
#select random integer either 0 or 1 for each spot in the list
#maybe a return at the end would work

#function to check solvability
#check is coordinates on all side = 1 or 0
#if it = 0 add it to stack
#add current location to visited
#go to location in stack and repeat until you reach the end (return true) or its not solvable
#if its not solvable return false
def isSolvable(grid_row, grid_col):
    size = len(grid_row) - 1
    visited = set()
    stack = [(0,0)]

    while stack:
        x, y = stack.pop()

        if x == size -1 and y == size -1:
            return True
        
        if (x,y) in visited:
            continue

        visited.add((x,y))

        if x < size -1 and grid_col[y][x+1] == 0:
            stack.append((x+1,y))

        if y < size -1 and grid_row[y+1][x] == 0:
            stack.append((x,y+1))

        if x > 0 and grid_col[y][x] == 0:
            stack.append((x-1,y))

        if y > 0 and grid_row[y][x] == 0:
            stack.append((x,y-1))

    return False

#draw maze function
#for every list and every spot in that list, check if it is a 1 or a 0, if it is a 1 then pen down and go forward, if 0 penup and forward 100
#always start from left or bottom
def draw(grid_row, grid_col):
        switch = -200
        for row in grid_row:
            for spot in row:
                if spot == [1]:
                    turtle.pendown()
                    turtle.forward(100)
                    turtle.penup()
                elif spot == [0]:
                    turtle.penup()
                    turtle.forward(100)
            switch+=100
            turtle.goto(-300,switch) 
        turtle.left(90)
        turtle.goto(-200,-300)
        switch = -200
        for col in grid_col:
            for spot in col:
                if spot == [0]:
                    turtle.penup()
                    turtle.forward(100)
                elif spot == [1]:
                    turtle.pendown()
                    turtle.forward(100)
                    turtle.penup()
            switch+=100
            turtle.goto(switch, -300)

turtle.speed(5)
turtle.penup()
turtle.goto(-300,-300)
turtle.forward(100)
turtle.pendown()
turtle.forward(500)
turtle.left(90)
turtle.forward(600)
turtle.left(90)
turtle.penup()
turtle.forward(100)
turtle.pendown()
turtle.forward(500)
turtle.left(90)
turtle.forward(600)
turtle.penup()

turtle.goto(-300,-200)
turtle.left(90)
isSolvable(grid_row, grid_col)
if isSolvable == True:
    draw(grid_row, grid_col)
    

turtle.done()

#while true loop, inside is function call for wall gen, then if solvable function is called, if it returns true, draw maze function (and break?), if it returns false continue the while loop.