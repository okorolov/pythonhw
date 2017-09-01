#!/usr/bin/python3

import random

# Variables

board = []
ships = [4,3,3,2,2,2,1,1,1,1]

# Creating a clean board, made of 10 empty nested lists

for i in range(10):
    board.append([])
for i in board:
    for j in range(10):
        board[j].append('O')

# Function to check the position of the ship and to place it

def place_check(placeX1,placeY1,placeP,ship):
    placeX2 = placeX1
    placeY2 = placeY1

    # Verify how we should place the ship - horizontal or vertical

    if placeP == 2: placeX2,placeY2=placeX2+1,placeY2+ship
    else: placeX2,placeY2=placeX2+ship,placeY2+1
    if placeX2 > 10 or placeY2 > 10: return False

    # Verify if poisition and nearby locations are busy

    for i in board[placeX1-1:placeX2+1]:
        for j in i[placeY1-1:placeY2+1]:
            if j != 'O':
                return False

    # Place the ship on the board if all checks are ok

    for i in range(placeX1,placeX2):
        for j in range(placeY1,placeY2):
            board[i][j]='S'

    return True

# Function to place all the ships

def place_ship():
    counter = 10

    # Generate random initial position for the ship

    while counter != 0:
        for ship in ships:
            placeX1 = random.randint(1,10)
            placeY1 = random.randint(1,10)
            placeP = random.randint(1,2)

            # Call the place and check function

            if place_check(placeX1,placeY1,placeP,ship) == True:
                ships.remove(ship)
                counter-=1


#Call the function to fill the board

place_ship()

# Draw the filled board
def draw_filled_board():
    c = 0
    print(' ', end = '')
    print(''.join('{:>3}'.format(str(i)) for i in range(10)))
    for i in board:
        print (c, end = '')
        c+=1
        for j in i:
            print('{:>3}'.format(j), end = '')
        print()

draw_filled_board()

# Function for the game

def game():
    score = 0
    while score != 20:
        user_shotY,user_shotX = input().split()
        if board[int(user_shotX)][int(user_shotY)]=='S':
            print('HIT')
            score+=1
        else:
            print('miss((')
    print('YOU WIN')

# Start the game

game()
