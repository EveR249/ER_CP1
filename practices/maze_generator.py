#ER 2nd MAZE GENERATOR
import turtle
import random

#create respective wall lists
row_wall = ["|"," "]
col_wall = ["_"," "]

#create empty maze
row_grid = [[random.choice(row_wall),random.choice(row_wall),random.choice(row_wall),random.choice(row_wall),random.choice(row_wall),random.choice(row_wall)],
            [random.choice(row_wall),random.choice(row_wall),random.choice(row_wall),random.choice(row_wall),random.choice(row_wall),random.choice(row_wall)],
            [random.choice(row_wall),random.choice(row_wall),random.choice(row_wall),random.choice(row_wall),random.choice(row_wall),random.choice(row_wall)],
            [random.choice(row_wall),random.choice(row_wall),random.choice(row_wall),random.choice(row_wall),random.choice(row_wall),random.choice(row_wall)],
            [random.choice(row_wall),random.choice(row_wall),random.choice(row_wall),random.choice(row_wall),random.choice(row_wall),random.choice(row_wall)],
            [random.choice(row_wall),random.choice(row_wall),random.choice(row_wall),random.choice(row_wall),random.choice(row_wall),random.choice(row_wall)]]

col_grid = []
for row in row_grid:
    print(row)
