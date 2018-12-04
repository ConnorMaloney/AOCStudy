# Day 2 of Advent Calendar code problem - Part 1

file = open("in.txt","r")
strArr = file.readlines()
idArr = []
testArr = ['abcdef','bababc','abbcde','abcccd','aabcdd','abcdee','ababab']
testArr2 = ['abcde','fghij','klmno','pqrst','fguij','axcye','wvxyz']

# Grabs file lines and puts them into list, removes newline characters
for x in range(len(strArr)):
    y = strArr[x].replace('\n', '')
    idArr.append(y)

# Iterate through list, only counting letters that occur exactly twice, or exactly once
#print(idArr)
#print(testArr)

'''Part 1

# Counters for how many times characters appear
twice = 0
thrice = 0
twiceFlag = False
thriceFlag = False
checksum = 0

# Iterate through array of box id's
for x in range(len(idArr)):
    charsInStr = set() # Setup characters to be counted
    testStr = idArr[x]
    print(testStr + " has:")

    # Grab only characters from string 
    for i in range(len(testStr)):
        charsInStr.add(testStr[i])
    
    twiceFlag = False
    thriceFlag = False
    # Print occurrences of said character in each string
    for i in range(len(charsInStr)):
        char = charsInStr.pop()
        print(testStr.count(char), char)

        # Count twice of char only once
        if testStr.count(char) == 2 and twiceFlag == False:
            twice = twice + 1
            twiceFlag = True
        # Count thrice of char only once
        if testStr.count(char) == 3 and thriceFlag == False:
            thrice = thrice + 1
            thriceFlag = True
        # If both are hit, we can stop checking
        if twiceFlag == True and thriceFlag == True:
            break

checksum = twice * thrice
print("\n\n\n%i times %i = %i (Checksum)" % (twice,thrice,checksum))

# ANSWER WAS 6944 BABYYY
'''
# I have to compare each box ID string and find the two boxes
# that have a one character difference. I then have to remove that
# character and print out all of the other common characters.

# abc
# abf

def failsCheck(str1, str2):
    #print(str1, str2)
    if str1 == str2:
        #print("Same string, skipping")
        return False
    
    # Else, we try to iterate
    fail = 0
    for i in range(len(str1)):
        
        # Amount of times chars in same position dont match up
        if str1[i] != str2[i]:
            fail = fail + 1
            
    if fail <= 1:
        return True

    else:
        return False

'''
# This code is unnecessary, I have enough to solve the solution
def removeOddChar(str1, str2):
    for i in range(len(str1)):
        # Amount of times chars in same position dont match up
        if str1[i] != str2[i]:
            return 
'''


# Iterate through array of id's
for x in range(len(idArr)):
    #print(idArr[x])
    # this iterates 7781250 max times, wew

    # Compare curr id with every other id
    for y in range(len(idArr)):
        if (failsCheck(idArr[x], idArr[y]) == True):
            print("Success!")
            print(idArr[x], idArr[y])
            # If it passed the test...find the discrepancy


