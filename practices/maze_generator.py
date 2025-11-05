#ER 2nd MAZE GENERATOR
import turtle
import random

turtle.Turtle()

grid_row = []
grid_col = []

#get turtle to check if pen needs to be down or not and move the distance
def draw(grid_row, grid_col):
    for row in grid_row:
        for spot in row:
            if spot == 1:
                turtle.pendown()
                turtle.forward(100)
            if spot == 0:
                turtle.penup()
                turtle.forward(100)
    for col in grid_col:
        for spot in col:
            if spot == 1:
                turtle.pendown()
                turtle.forward(100)
            if spot == 0:
                turtle.penup()
                turtle.forward(100)

#check if maze is solvable
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


x=0

while x<1:
    grid_row = [[[random.randint(0,1)],[random.randint(0,1)],[random.randint(0,1)],[random.randint(0,1)],[random.randint(0,1)],[random.randint(0,1)]],
             [[random.randint(0,1)],[random.randint(0,1)],[random.randint(0,1)],[random.randint(0,1)],[random.randint(0,1)],[random.randint(0,1)]],
             [[random.randint(0,1)],[random.randint(0,1)],[random.randint(0,1)],[random.randint(0,1)],[random.randint(0,1)],[random.randint(0,1)]],
             [[random.randint(0,1)],[random.randint(0,1)],[random.randint(0,1)],[random.randint(0,1)],[random.randint(0,1)],[random.randint(0,1)]],
             [[random.randint(0,1)],[random.randint(0,1)],[random.randint(0,1)],[random.randint(0,1)],[random.randint(0,1)],[random.randint(0,1)]],
             [[random.randint(0,1)],[random.randint(0,1)],[random.randint(0,1)],[random.randint(0,1)],[random.randint(0,1)],[random.randint(0,1)]]]

    grid_col = [[[random.randint(0,1)],[random.randint(0,1)],[random.randint(0,1)],[random.randint(0,1)],[random.randint(0,1)],[random.randint(0,1)]],
             [[random.randint(0,1)],[random.randint(0,1)],[random.randint(0,1)],[random.randint(0,1)],[random.randint(0,1)],[random.randint(0,1)]],
             [[random.randint(0,1)],[random.randint(0,1)],[random.randint(0,1)],[random.randint(0,1)],[random.randint(0,1)],[random.randint(0,1)]],
             [[random.randint(0,1)],[random.randint(0,1)],[random.randint(0,1)],[random.randint(0,1)],[random.randint(0,1)],[random.randint(0,1)]],
             [[random.randint(0,1)],[random.randint(0,1)],[random.randint(0,1)],[random.randint(0,1)],[random.randint(0,1)],[random.randint(0,1)]],
             [[random.randint(0,1)],[random.randint(0,1)],[random.randint(0,1)],[random.randint(0,1)],[random.randint(0,1)],[random.randint(0,1)]]]
   
    
    #isSolvable(grid_row, grid_col)
    #if isSolvable == False:
        #continue

    draw(grid_row, grid_col)
    turtle.done
    x+=1
