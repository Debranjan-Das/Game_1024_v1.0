# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 05:03:42 2022

@author: debranjan

Assumption: (1) Only the digit 2 appears at empty position after a turn ends
(2) 1024 is the winning value
"""

import numpy as np
import random

# Fuction to randomly fill the number 2 at an empty position after turn ends
def random_fill_2 (a):
    empty_pos = []
    for i in range (0,4):
        for j in range (0,4):
            if (a[i][j] == 0):
                empty_pos.append(int((i*10)+j)) # records the position of matrix which is empty
    if (len(empty_pos) != 0):
        fill_pos = random.choice (empty_pos) #randomly chooses an empty position of the matrix 
        for i in range (0,4):
            for j in range (0,4):
                if (((i*10)+j) == fill_pos):
                    a[i][j] = 2 #replaces null with 2 on the randomly selected position
        return a
    else:
        return a

# Function to get results after swiping up
def result_up (a):
    for j in range (0,4):
        count_zero = 0
        for i in range (0,4):
            if (a[i][j] == 0):
                count_zero = count_zero + 1
        if (count_zero == 4):
            continue # Rejects rest of the loop if all element in column are 0
        elif (count_zero == 3):
            a[0][j] = a[0][j]+a[1][j]+a[2][j]+a[3][j]
            a[1][j] = a[2][j] = a[3][j] = 0
        elif (count_zero == 2):
            nonzero_index = np.nonzero([a[0][j],a[1][j],a[2][j],a[3][j]])[0] # Counts the number of non-zero elements in the column
            if (a[nonzero_index[0]][j] == a[nonzero_index[1]][j]):
                a[0][j] = a[nonzero_index[0]][j] * 2
                a[1][j] = a[2][j] = a[3][j] = 0
            else:
                a[0][j] = a[nonzero_index[0]][j]
                a[1][j] = a[nonzero_index[1]][j]
                a[2][j] = a[3][j] = 0
        elif (count_zero == 1):
            if (a[0][j] == 0):
                a[0][j] = a[1][j]
                a[1][j] = a[2][j]
                a[2][j] = a[3][j]
                a[3][j] = 0
                if (a[1][j] == a[0][j]):
                    a[0][j] = a[1][j] * 2
                    a[1][j] = a[2][j]
                    a[2][j] = 0
                elif (a[1][j] == a[2][j]):
                    a[1][j] = a[2][j] * 2
                    a[2][j] = 0
            elif (a[1][j] == 0):
                a[1][j] = a[2][j]
                a[2][j] = a[3][j]
                a[3][j] = 0
                if (a[1][j] == a[2][j]):
                    a[1][j] = a[2][j] * 2
                    a[2][j] = 0
                elif (a[1][j] == a[0][j]):
                    a[0][j] = a[1][j] * 2
                    a[1][j] = a[2][j]
                    a[2][j] = 0
            elif (a[2][j] == 0):
                a[2][j] = a[3][j]
                a[3][j] = 0
                if (a[1][j] == a[2][j]):
                    a[1][j] = a[2][j] * 2
                    a[2][j] = 0
                elif (a[1][j] == a[0][j]):
                    a[0][j] = a[1][j] * 2
                    a[1][j] = a[2][j]
                    a[2][j] = 0
            else:
                if (a[1][j] == a[2][j]):
                    a[1][j] = a[2][j] * 2
                    a[2][j] = 0
                elif (a[1][j] == a[0][j]):
                    a[0][j] = a[1][j] * 2
                    a[1][j] = a[2][j]
                    a[2][j] = 0                
        else:
            if (a[0][j] == a[1][j] and a[2][j] == a[3][j]):
                a[0][j] = a[1][j] * 2
                a[1][j] = a[2][j] * 2
                a[2][j] = a[3][j] = 0
            elif (a[0][j] == a[1][j] and a[2][j] != a[3][j]):
                a[0][j] = a[1][j] * 2
                a[1][j] = a[2][j]
                a[2][j] = a[3][j]
                a[3][j] = 0
            elif (a[0][j] != a[1][j] and a[2][j] == a[3][j]):
                a[2][j] = a[3][j] * 2
                a[3][j] = 0
            elif (a[1][j] == a[2][j]):
                a[1][j] = a[2][j] * 2
                a[2][j] = a[3][j]
                a[3][j] = 0
    return a

# The below three function uses result_up function to compute
# These three function transform given matrix into result_up intial matrix

def result_left (a):
    temp = np.zeros(shape=(4,4))
    temp = result_up(a.transpose())
    return temp.transpose()  

def result_right (a):
    temp = np.zeros(shape=(4,4))
    temp = result_left(np.flip(a,axis=1))
    return np.flip(temp,axis=1)

def result_down (a):
    temp = np.zeros(shape=(4,4))
    temp = result_up(np.flip(a,axis=0))
    return np.flip(temp,axis=0)

# Starting board with two randomly placed 2's represented by variable matrix
matrix = random_fill_2 (random_fill_2 (np.zeros(shape=(4,4))))
print ("Starting Board: \n", matrix)
game_status = 'In-Progress'
no_of_turns = 0

while (game_status == 'In-Progress'):
    status_update = 0
    no_of_turns = no_of_turns + 1
    actual_matrix = np.zeros(shape=(4,4))
    actual_matrix = matrix
    # Input prompt to get the next move
    movement = input("Enter the next swipe move: w: up, a: left, d: right, s: down: ") 
    if (movement == 'w'):
        print ('Board after Turn: ', no_of_turns, '\n')
        """if (np.allclose(actual_matrix, result_up(matrix))):
            print ('Move is invalid \n')
            continue"""
        print (random_fill_2(result_up(matrix)))
    elif (movement == 'a'):
        print ('Board after Turn: ', no_of_turns, '\n')
        print (random_fill_2(result_left(matrix)))
    elif (movement == 'd'):
        print ('Board after Turn: ', no_of_turns, '\n')
        print (random_fill_2(result_right(matrix)))
    elif (movement == 's'):
        print ('Board after Turn: ', no_of_turns, '\n')
        print (random_fill_2(result_down(matrix)))
    
    # Checking the status of the game    
    # Checking if 1024 is reached which is the winning number
    for i in range (0,4):
        for j in range (0,4):
            if (matrix[i][j] == 1024):
                game_status = 'Congrats have won!'
                print ('Congrats have won!')
                status_update = status_update + 1
                continue
    # Checking if there is an empty position
    for i in range (0,4):
        for j in range (0,4):
            if (matrix[i][j] == 0):
                game_status = 'In-Progress'
                status_update = status_update + 1
                continue
    # Checking if after swiping in any direction there will be an empty position
    for i in range (0,3):
        for j in range (0,3):
            if (matrix[i][j] == matrix[i][j+1] or matrix[i][j] == matrix[i+1][j]):
                game_status = 'In-Progress'
                status_update = status_update + 1
                continue
    for j in range (0,3):
        if (matrix[3][j] == matrix[3][j+1]):
            game_status = 'In-Progress'
            status_update = status_update + 1
            continue
    for i in range (0,3):
        if (matrix[i][3] == matrix[i+1][3]):
            game_status = 'In-Progress'
            status_update = status_update + 1
            continue
    # If none of above condition is true it means there is no space to have a random 2 for next turn
    if (status_update == 0):
        print('Alas! you have lost the game')
        game_status = 'Game Over!'
        break