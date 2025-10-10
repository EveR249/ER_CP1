import random

board = [[1,2,3],
         [4,5,6],
         [7,8,9]]

print(board)

row = int(input("What row do you choose? ")) +1
column = int(input("What column do you choose? ")) +1
board[row][column] = "X"

comprow = random.randint(1,4)
compcolumn = random.randint(1,4)
board[row][column] = "O"