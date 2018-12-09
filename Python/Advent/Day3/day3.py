# Day 3 of Advent Calendar code problem - Part 1

import sys
from pprint import pprint
file = open("in.txt","r")
str_arr = file.readlines()
claim_arr = []

# Creates 2D patch array initialized with dots
#patch_arr = [['.' for x in range(1000)] for y in range(1000)]
# Grabs file lines and puts them into list, removes newline characters
for x in range(len(str_arr)):
    y = str_arr[x].replace('\n', '')
    claim_arr.append(y)

#print(claim_arr)
    

# HOW THE HELL AM I SUPPOESD TO DO PART 2 LOL

# I'll need to use classes.
test_patch_arr = [['.' for x in range(10)] for y in range(10)]
test_claim_arr = ['#1 @ 1,3: 4x4', '#2 @ 3,1: 4x4', '#3 @ 5,5: 2x2']
square_arr = [] # This array will store all square patch objects

class Patch:
    def __init__(self, patch_id, squares_taken):
        self.patch_id = patch_id
        self.squares_taken = squares_taken
# Take in claim data and spit out useful data (id coord, coords of patch and size of patch)
for i in range(len(test_claim_arr)):
    data = test_claim_arr[i].split()

    id = data[0] # Grab patch id
    del data[1] # Remove @ symbol

    del data[0]

    # Grab coord and dimension data
    
    x_coord_data = int((data[0].split(','))[0])
    y_coord_data = int((data[0].split(','))[1].rstrip(':'))
    x_length = int(data[1].split('x')[0])
    y_height = int(data[1].split('x')[1])

    squares_taken = [] # Define list to show all square coords taken by patch

    for x in range(x_coord_data, (x_coord_data + x_length)):
        for y in range(y_coord_data, (y_coord_data + y_height)):
            square = float(str(x) + '.' + str(y))
            squares_taken.append(square)

    squarePatch = Patch(id, squares_taken)
    square_arr.append(squarePatch)


#pprint(vars(square_arr[0]))

for i in range(len(square_arr)):
    checkSquare = square_arr[i]
    print(vars(checkSquare))
    for j in range(len(checkSquare.squares_taken)):
        checkCoord = checkSquare.squares_taken[j]
        print(checkCoord)
    

#set_squares = set(square_arr)
#print(', '.join(set_squares))
'''
for i in range(len(square_arr)):
    for j in range(len(square_arr)):
        for k in range(len(square_arr[j].squares_taken)):
            #print(square_arr[j].squares_taken[k])
            if (square_arr[j].squares_taken[k] in square_arr[i].squares_taken):
                print("found")
            '''


    



'''
#PART 1

# Whole piece of fabric is atleast 1000x1000 inches.
# Each elf makes a claim of which area of said fabric is best.
# Claims have an ID, specify area of rectangle. 
# ClaimID: @ 3 inches (x coor), 2 inches (y coor). 5 wide and 4 tall.
# Problem: Some claims overlap.

# claimIDArr = [] # I don't know if claim ID's will be necessary


# Pretty print patch array
def printPatchArr(my_arr):
    santas_strip = ''
    for i in range(len(my_arr)):
        patch_row = str(my_arr[i])
        # I dont fully understand what this line is doing, but ey it removes the gross chars
        patch_row = patch_row.translate({ord(c): None for c in '[\',] '})
        santas_strip = santas_strip + patch_row + '\n' 
    print(santas_strip)

# Count collisions (!'s)
def countCollisions(my_arr):
    num_collisions = 0
    for i in range(len(my_arr)):
        for j in range(len(my_arr)):
            if my_arr[i][j] == '!':
                num_collisions = num_collisions + 1
    print("\n" + str(num_collisions) + " COLLISIONS FOUND\n")

def runTest():
    test_patch_arr = [['.' for x in range(10)] for y in range(10)]
    test_claim_arr = ['#1 @ 1,3: 4x4', '#2 @ 3,1: 4x4', '#3 @ 5,5: 2x2']
    # Take in claim data and spit out useful data (coords of patch and size of patch)
    for i in range(len(test_claim_arr)):
        data = test_claim_arr[i].split()

        # Remove first claim ID and @ symbols from array
        del data[0]
        del data[0]
        #print(data)

        # Grab coord and dimension data
        x_coord_data = int((data[0].split(','))[0])
        y_coord_data = int((data[0].split(','))[1].rstrip(':'))
        x_length = int(data[1].split('x')[0])
        y_height = int(data[1].split('x')[1])

        # This plots where the elves want to cut.
        # . indicates empty, X indicates taken, ! indicates collision
        for x in range(x_coord_data, x_coord_data + x_length):
            for y in range(y_coord_data, y_coord_data + y_height):
                if test_patch_arr[x][y] == '.':
                    test_patch_arr[x][y] = 'X'
                elif test_patch_arr[x][y] == 'X':
                    test_patch_arr[x][y] = '!'
        
    printPatchArr(test_patch_arr)
    countCollisions(test_patch_arr) # GOT IT, Answer was 120419

def run():
    patch_arr = [['.' for x in range(1000)] for y in range(1000)]
    #test_claim_arr = ['#1 @ 1,3: 4x4', '#2 @ 3,1: 4x4', '#3 @ 5,5: 2x2']
    # Take in claim data and spit out useful data (coords of patch and size of patch)
    for i in range(len(claim_arr)):
        data = claim_arr[i].split()

        # Remove first claim ID and @ symbols from array
        del data[0]
        del data[0]
        #print(data)

        # Grab coord and dimension data
        x_coord_data = int((data[0].split(','))[0])
        y_coord_data = int((data[0].split(','))[1].rstrip(':'))
        x_length = int(data[1].split('x')[0])
        y_height = int(data[1].split('x')[1])

        # This plots where the elves want to cut.
        # . indicates empty, X indicates taken, ! indicates collision
        for x in range(x_coord_data, x_coord_data + x_length):
            for y in range(y_coord_data, y_coord_data + y_height):
                if patch_arr[x][y] == '.':
                    patch_arr[x][y] = 'X'
                elif patch_arr[x][y] == 'X':
                    patch_arr[x][y] = '!'
        
    printPatchArr(patch_arr)
    countCollisions(patch_arr) # GOT IT, Answer was 120419


#runTest()
#run()

'''
    


