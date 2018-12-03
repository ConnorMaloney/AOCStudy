# Day 1 of Advent Calendar code problem - Part 1

file = open("in.txt","r")
strArr = file.readlines()
newArr = []
ansArr = []
#print(len(strArr))
# Converts file of strings into new number array
for x in range(len(strArr)):
    y = strArr[x].replace('\n', '')
    #print(y)
    newArr.append(y)


answer = 0
for y in range(len(newArr)):
    answer = answer + int(newArr[y])
    ansArr.append(answer)
# 592 - print(answer)

''' Part 1 finished. 592 is the result of all the frequency changes '''

# -----------------------------------------------------

# Part 2
# Does the array actually have an equal amount of duplicate frequencies and contents?
# print(len(set(ansArr))) - 973, same amount of lines in input file
# So is this saying there are no duplicate frequency answers?!
'''
print(len(strArr))
print(len(newArr))
print(len(ansArr))
print(len(set(newArr)))
print(len(set(ansArr)))
ansArr.sort()
print(set(ansArr))
'''

# OHHHH, it means to loop OVER all the changes AGAIN until it hits a duplicate.
# Not in one sitting. Gotcha

#finalAns = ansArr2 + ansArr
#print(len(finalAns)) - 1946
#print(len(set(finalAns))) - 1946

# What I need to do is iterate through all 973 times, checking for duplicates
# each time I run through. Once I hit 973, repeat the whole process again
# while still keeping the same answer. Break out of the loop until I hit
# a duplicate.



'''
Code I made in python interpreter to make an array circular
nums = [1, 2, 3, 40]
pos = 0
while True:
    if pos == len(nums):
        print("Reset!")
        pos = 0
    else:
        print(nums[pos])
        pos = pos + 1
'''

# Wow, still no duplicate frequency found after a second iteration.
# This will be tougher then I thought.

#print(int(newArr[0]) + int(newArr[1]) + int(newArr[2]))
# Since were only checking for the FIRST duplicate, I don't need to use a set.
# I can just store every single frequency, and then compare if an old frequency is equal to the new result.


#print(newArr)
pos = 0
part2ans = 0
freqArr = []
# This loops over the answer array in a circular manner
for i in range(10000000):
    if pos == len(newArr):
        pos = 0 # Loop back to beginning of calculations
    else:
        part2ans = part2ans + int(newArr[pos]) # Calculate frequency

        # If duplicate is found
        if part2ans in freqArr:
            print("Frequency has appeared twice!")
            print(part2ans)
            break

        else:
            freqArr.append(part2ans) # Append frequency to array
            pos = pos + 1 # Iterate


# print((set(freqArr) == freqArr)) # If true then they are all unique. Its false though. So Im missing something...
#freqArrDuplicates = set([x for x in freqArr if freqArr.count(x) > 1]) # prints set of duplicate frequencies found
#print(freqArrDuplicates)

# 241 BAAABYYYYY

'''
#Test code, this algorithm seems to work for the practice examples of part2

pos = 0
ans = 0
nums = [+7,+7,-2,-7,-4]
freqs = []
for i in range(20):
    if pos == len(nums):
        pos = 0 # Loop back to beginning of calculations
    else:
        ans = ans + int(nums[pos]) # Calculate frequency

        # This condition doesn't seem to ever be hitting...
        if ans in freqs:
            print("num has appeared twice!")
            print(ans)
            break
        #else:
            #print("nah")
        freqs.append(ans) # Append frequency to array
        pos = pos + 1 # Iterate
'''
