#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 17:45:09 2019

@author: lingyinghan
"""

x = -99
epsilon = 0.01
numGuesses = 0
high = 0
low = x
ans = (high + low)/2.0
while abs(ans**3 - x) >= epsilon:
    print('low =' + str(low) + 'high=' + str(high) + 'ans=' + str(ans))
    numGuesses +=1
    if ans**3 > x:
        high = ans
    else:
        low = ans
    ans=(high + low)/2.0
print ('numGuesses=' + str(numGuesses))
print (str(ans) + 'is close to cube root of' + str(x))