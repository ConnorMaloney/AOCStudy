# Day 3 of Advent Calendar code problem - Part 1

import sys
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

class Patch:
    def __init__(self, patch_id, coords, size):
        self.patch_id = patch_id
        self.coords = coords
        self.size = size

#patch1 = Patch(1, [[1,2], [2,4] ,[5,6]])

#print(patch1.patch_id)



'''

PART 1

# Whole piece of frabic is atleast 1000x1000 inches.
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
'''

    


