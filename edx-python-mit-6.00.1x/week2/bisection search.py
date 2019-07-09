#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 16:59:14 2019

@author: lingyinghan
"""

x = 64
epsilon = 0.01
numGuesses = 0
low = 0
high = x
ans = (high + low)/2.0
while abs(ans**2-x) >= epsilon:
    print('low=' + str(low) + 'high=' + str(high) + 'ans=' + str(ans))
    numGuesses +=1
    if ans **2 < x:
        low = ans
    else:
        high = ans
    ans=(high + low)/2.0
print ('numGuesses=' + str(numGuesses))
print (str(ans) + 'is close to square root of ' + str(x))

x = 27
epsilon = 0.01
numGuesses = 0
low = 0
high = x
ans = (high + low)/2.0
while abs(ans**3 - x) >= epsilon:
    print('low =' + str(low) + 'high=' + str(high) + 'ans=' + str(ans))
    numGuesses +=1
    if ans**3 < x:
        low = ans
    else:
        high = ans
    ans=(high + low)/2.0
print ('numGuesses=' + str(numGuesses))
print (str(ans) 'is close to cube root of' + str(x))

cube = 27
epsilon = 0.01
num_guesses = 0
low = 0
high = cube
guess = (high+low)/2.0
while abs(guess**3 - cube) >= epsilon:
    if guess**3<cube:
        low = guess
    else:
        high = guess
    guess = (high+low)/2.0
    num_guesses += 1
print ('num_guesses=', num_guesses)
print (guess, 'is close to the cube root of', cube)