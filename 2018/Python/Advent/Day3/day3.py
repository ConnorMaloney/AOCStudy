# Day 3 of Advent Calendar code problem - Part 1


# Guess 1: FAIL. 101 too low?

# NOTE: There are times where it is skipping. It is supposed to do that, but not this few amount of times
# Nevermind, its skipping future id's that already have encountered a collission. 
# But my implementation only accounts for half of them.
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

# HOW THE HELL AM I SUPPOESD TO DO PART 2 LOL

# I'll need to use classes.
#test_patch_arr = [['.' for x in range(15)] for y in range(15)]
test_claim_arr = ['#1 @ 520,746: 4x20',
'#2 @ 274,680: 19x26',
'#3 @ 928,402: 16x24',
'#4 @ 338,969: 27x15',
'#5 @ 48,306: 21x16',
'#6 @ 418,87: 13x20',
'#7 @ 271,316: 16x20',
'#8 @ 697,513: 20x25',
'#9 @ 120,479: 28x13',
'#10 @ 974,8: 17x12',
'#11 @ 615,355: 11x29',
'#12 @ 687,970: 20x29',
'#13 @ 176,605: 24x11',
'#14 @ 512,252: 11x11',
'#15 @ 839,821: 20x10',
'#16 @ 242,267: 29x14',
'#17 @ 702,795: 11x14',
'#18 @ 695,516: 14x18',
'#19 @ 108,169: 28x12',
'#20 @ 13,973: 27x18',
'#21 @ 1,580: 14x28',
'#22 @ 319,694: 19x27',
'#23 @ 149,828: 11x23',
'#24 @ 619,935: 11x26',
'#25 @ 727,746: 6x3',
'#26 @ 808,336: 21x17',
'#27 @ 71,335: 10x17',
'#28 @ 335,307: 16x19',
'#29 @ 524,551: 18x17',
'#30 @ 486,831: 16x28',
'#31 @ 193,548: 22x29',
'#32 @ 29,815: 20x18',
'#33 @ 719,847: 26x24',
'#34 @ 721,350: 19x18',
'#35 @ 870,260: 10x20',
'#36 @ 246,702: 29x27',
'#37 @ 342,892: 16x22',
'#38 @ 919,512: 25x13',
'#39 @ 646,154: 23x13',
'#40 @ 573,181: 21x25',
'#41 @ 175,929: 29x17',
'#42 @ 694,104: 10x13',
'#43 @ 778,869: 27x21',
'#44 @ 296,748: 23x29',
'#45 @ 139,481: 29x18',
'#46 @ 228,790: 29x23',
'#47 @ 497,517: 12x24',
'#48 @ 753,926: 12x11',
'#49 @ 234,780: 17x28',
'#50 @ 932,553: 12x17',
'#51 @ 584,9: 12x20',
'#52 @ 57,516: 29x28',
'#53 @ 788,669: 29x18',
'#54 @ 188,303: 25x20',
'#55 @ 281,262: 20x28',
'#56 @ 98,714: 28x11',
'#57 @ 900,534: 12x22',
'#58 @ 660,720: 27x10',
'#59 @ 754,940: 25x27',
'#60 @ 867,499: 23x24',
'#61 @ 0,941: 16x10',
'#62 @ 855,807: 10x23',
'#63 @ 122,283: 22x19',
'#64 @ 940,539: 15x22',
'#65 @ 223,971: 22x26',
'#66 @ 784,516: 21x26',
'#67 @ 395,354: 13x28',
'#68 @ 566,199: 25x18',
'#69 @ 78,648: 3x15',
'#70 @ 11,971: 18x11',
'#71 @ 442,407: 5x17',
'#72 @ 224,61: 24x14',
'#73 @ 71,380: 26x28',
'#74 @ 528,411: 26x14',
'#75 @ 653,973: 19x25',
'#76 @ 76,329: 12x18',
'#77 @ 59,295: 11x22',
'#78 @ 597,430: 18x25',
'#79 @ 512,533: 28x23',
'#80 @ 523,946: 20x17',
'#81 @ 485,575: 10x26',
'#82 @ 455,563: 16x29',
'#83 @ 450,846: 13x17',
'#84 @ 305,601: 19x22',
'#85 @ 579,715: 7x16',
'#86 @ 553,26: 25x21',
'#87 @ 593,174: 21x16',
'#88 @ 551,427: 12x16',
'#89 @ 581,266: 22x13',
'#90 @ 362,647: 12x18',
'#91 @ 209,850: 12x15',
'#92 @ 483,327: 12x12',
'#93 @ 570,825: 10x15',
'#94 @ 598,903: 14x28',
'#95 @ 248,136: 11x16',
'#96 @ 94,631: 13x23',
'#97 @ 230,226: 16x23',
'#98 @ 737,891: 13x18',
'#99 @ 720,613: 26x15',
'#100 @ 62,620: 23x14']


# Potential bug? 4x40 reports 16 collissions (which it shouldn't), whereas 40x4 reports 12 (which it should)
small_test_claim_arr = ['#1 @ 1,3: 4x8',
'#2 @ 3,1: 4x4',
'#3 @ 5,5: 2x2']

test_patch_arr = [['.' for x in range(1000)] for y in range(1000)]

square_arr = [] # This list will store all square patch objects

# This set will store all unique coords, effectively "breaking" many square patches that have duplicates.
# With this, we can then compare all of these unique coords to see if any parition of those coords fits with an id.
all_coords_taken = []
unique_coords = set()
collision_coords = [] # Define set of containing all collision coords (where X's occur)

# Define class Patch object
class Patch:
    def __init__(self, patch_id, coords_taken, has_collision):
        self.patch_id = patch_id
        self.coords_taken = coords_taken
        self.has_collision = has_collision

    
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

# Take in claim data and spit out useful data (id coord, coords of patch and size of patch), also populate array
for i in range(len(claim_arr)):
    data = claim_arr[i].split()
    id = data[0] # Grab patch id
    del data[1] # Remove @ symbol
    del data[0]
    # Grab coord and dimension data
    x_coord_data = int((data[0].split(','))[0])
    y_coord_data = int((data[0].split(','))[1].rstrip(':'))
    x_length = int(data[1].split('x')[0])
    y_height = int(data[1].split('x')[1])
    coords_taken = [] # Define list to show all coords taken by patch

    squarePatch = Patch(id, coords_taken, False)

    for x in range(x_coord_data, x_coord_data + x_length):
        for y in range(y_coord_data, y_coord_data + y_height):
            if test_patch_arr[x][y] == '.':
                test_patch_arr[x][y] = 'X'
            elif test_patch_arr[x][y] == 'X':
                test_patch_arr[x][y] = '!'
                collision_coords.append(float(str(x) + '.' + str(y)))
                
            coords = float(str(x) + '.' + str(y))
            coords_taken.append(coords)
            all_coords_taken.append(coords)
            unique_coords.add(coords)

    squarePatch = Patch(id, coords_taken, False)
    #print(vars(squarePatch))
    square_arr.append(squarePatch)

printPatchArr(test_patch_arr)
#countCollisions(test_patch_arr)
print(len(collision_coords))

print("\nChecking coordinates for collisions...")
for i in range(len(square_arr)):
    for j in range(len(square_arr[i].coords_taken)):
        #print(square_arr[i].coords_taken[j])#, square_arr[i].coords_taken)
        sys.stdout.write('\r>> %s %f' % (square_arr[i].patch_id, square_arr[i].coords_taken[j]))
        sys.stdout.flush()
        if (square_arr[i].has_collision == True):
            break
        if (square_arr[i].coords_taken[j] in collision_coords):
            square_arr[i].has_collision = True

for i in range(len(square_arr)):
    if square_arr[i].has_collision == False:
        print("\nNO COLLISIONS: ", square_arr[i].patch_id)

# LMAOOOO JUST FIGURED OUT THE ANSWER FOR PART 1 (aweh, nvm...but wait, shouldnt it be? It works for small_test_square_arr)

# this must mean that there is something wrong with the heart of my code. The algorithm above.
#print("Coordinates plotted: ", len(all_coords_taken))
#print("Unique coordinates: ", len(unique_coords))
#print("Number of X's (collisions): ", (len(all_coords_taken)) - (len(unique_coords)))


#for i in range(len(square_arr)):
    #print(square_arr[i].patch_id, square_arr[i].coords_taken)

# Optional pretty print: pprint(vars(square_arr[0]))
'''
# CHECK FOR COMPARISONS
for i in range(len(square_arr)):
    checkSquare = square_arr[i]
   # print(checkSquare.patch_id)
    for j in range(len(checkSquare.coords_taken)):
        # take this coord and check it through entire array
        checkCoord = checkSquare.coords_taken[j]
        # iterate through entire array and set flags
        for k in range(len(square_arr)):
            print(k)
            # only check patch id's that are different
            if checkSquare.patch_id != square_arr[k].patch_id:
                # Don't check whats already been given as collision

                # For some reason this just keeps printing out 1's or 0's if I include print(k). Without it, it functions as I would expect
                #if 'X' in square_arr[k].coords_taken:
                    #k = k + 1
                    #print(square_arr[k].patch_id, "has X")
                    #print(k)
                    #break

                #if 'X' in checkSquare.coords_taken:
                    #print(k)
                    #break
                
                #if 'X' in square_arr[k].coords_taken:
                 #   k = k + 1
                    #print(square_arr[k].patch_id, "has X")
                   # print(k)
                  #  break

                # Map out all collisions
                #if checkCoord == 'X':
                    #break
                
                # Check with flags
                #if checkSquare.has_collision == True:
                    #break
                if checkCoord in square_arr[k].coords_taken:
                    coordOfCollision1 = checkSquare.coords_taken.index(checkCoord)
                    coordOfCollision2 = square_arr[k].coords_taken.index(checkCoord)
                    #sys.stdout.write('\r>> %s %f %s' % (checkSquare.patch_id, checkCoord, square_arr[k].patch_id))
                    #sys.stdout.flush()
    
                    # set patch flags
                    checkSquare.has_collision = True
                    square_arr[k].has_collision = True
                    print(checkSquare.patch_id, checkCoord, square_arr[k].patch_id, square_arr[k].coords_taken[coordOfCollision2], "collision") 
                    checkSquare.coords_taken[coordOfCollision1] = 'X'
                    square_arr[k].coords_taken[coordOfCollision2] = 'X'
         


for l in range(len(square_arr)):
    #print(square_arr[l].patch_id, square_arr[l].has_collision)
    #if square_arr[l].has_collision == False:
        #print("\nNO COLLISIONS: ", square_arr[l].patch_id)

    if 'X' not in square_arr[l].coords_taken:
        print("\nNO COLLISIONS: ", square_arr[l].patch_id)
    
#for i in range(len(square_arr)):
    #print(square_arr[i].patch_id, square_arr[i].coords_taken)

#set_squares = set(square_arr)
#print(', '.join(set_squares))
'''
'''
for i in range(len(square_arr)):
    for j in range(len(square_arr)):
        for k in range(len(square_arr[j].coords_taken)):
            #print(square_arr[j].coords_taken[k])
            if (square_arr[j].coords_taken[k] in square_arr[i].coords_taken):
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
    


