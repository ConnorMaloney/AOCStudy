# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

''' 
Let a and b be positive integers such that ab + 1 divides a^2 + b^2.
Show that a^2 + b^2 / ab + 1 is the square of an integer. 
'''

import random
from math import sqrt

def question_six(a,b):
    return ((a**2 + b**2) / (a*b + 1))

def is_square(n):
    return sqrt(n).is_integer()


for x in range(1,100000001):
    a = random.randint(1,1001)
    b = random.randint(1,1001)
    #print(a,b)
    
    if (is_square(question_six(a,b))):
        print(a,b)
        