# Day 2 of Advent Calendar code problem - Part 1

file = open("in.txt","r")
strArr = file.readlines()
idArr = []
testArr = ['abcdef','bababc','abbcde','abcccd','aabcdd','abcdee','ababab']

# Grabs file lines and puts them into list, removes newline characters
for x in range(len(strArr)):
    y = strArr[x].replace('\n', '')
    #print(y)
    idArr.append(y)

# Iterate through list, only counting letters that occur exactly twice, or exactly once
#print(idArr)
#print(testArr)

'''TESTING'''
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

