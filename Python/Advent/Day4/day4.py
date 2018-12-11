# Day 4 of Advent Calendar code problem - Part 1
import sys # Used for printing multiple feeds to stdout on same line
from pprint import pprint # Used for pretty printing vars

# Read in input of in.txt
with open('in.txt') as f:
    sched_arr = f.read().splitlines() 

# First things first, I'll need to sort the array.
sched_arr = sorted(sched_arr)
# Well that was easy.

# Now I'll need to find the guard that sleeps the most, and then the minute he's spent sleeping the most.
# Each guard always sleeps/wakesup between 00:00-00:59. Basically they like to sleep for the first hour of their shift (or is their shift only one hour long)
# Oh, it seems to be that the person recording them only observes them for the hour

test_sched_arr = [
'[1518-11-01 00:00] Guard #10 begins shift',
'[1518-11-01 00:05] falls asleep',
'[1518-11-01 00:25] wakes up',
'[1518-11-01 00:30] falls asleep',
'[1518-11-01 00:55] wakes up',
'[1518-11-01 23:58] Guard #99 begins shift',
'[1518-11-02 00:40] falls asleep',
'[1518-11-02 00:50] wakes up',
'[1518-11-03 00:05] Guard #10 begins shift',
'[1518-11-03 00:24] falls asleep',
'[1518-11-03 00:29] wakes up',
'[1518-11-04 00:02] Guard #99 begins shift',
'[1518-11-04 00:36] falls asleep',
'[1518-11-04 00:46] wakes up',
'[1518-11-05 00:03] Guard #99 begins shift',
'[1518-11-05 00:45] falls asleep',
'[1518-11-05 00:55] wakes up'
]

#pprint(test_sched_arr)

class Guard:
    def __init__(self, guard_id, shifts):
        self.guard_id = guard_id
        self.shifts = shifts

    def time_slept(self):
        return 5


guard_arr = [] # Create empty guard array to store all guard objects, ordered by ID's
# Iterate through array
#for i in range(len(test_sched_arr)):


guard1 = Guard(5, ['[1518-11-05 00:03] Guard #99 begins shift',
'[1518-11-05 00:45] falls asleep',
'[1518-11-05 00:55] wakes up'])

#pprint(vars(guard1))
print("TOTAL TIME SLEPT: " + str(guard1.time_slept()))


