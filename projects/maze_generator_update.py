#ER 2nd Maze generator

#set variables
#Build functions
    #one function randomizes walls
    #one function checks if solvable
    #make sure you set start and stop correctly
    #Use path coordinates to check walls in each direction
#use turtle to draw the maze
#turtle moves the distance, you determins if pen is up or down
#need three functions

#set list of rows 6 "columns" inside each list, 6 lists inside a big list, each spot will be randomly assigned a 1 or a 0. same thing for columns

#Make a function to randomize walls
#Remember to import random
#select random integer either 0 or 1 for each spot in the list
#maybe a return at the end would work

#function to check solvability
#check is coordinates on all side = 1 or 0
#if it = 0 add it to stack
#add current location to visited
#go to location in stack and repeat until you reach the end (return true) or its not solvable
#if its not solvable return false

#draw maze function
#for every list and every spot in that list, check if it is a 1 or a 0, if it is a 1 then pen down and go forward, if 0 penup and forward 100

#while true loop inside is function call for wall gen, then if solvable function is called, if it returns true, draw maze function (and break?), if it returns false continue the while loop.