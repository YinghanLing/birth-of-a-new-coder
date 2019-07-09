#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 15 13:32:11 2018

@author: lingyinghan
"""

print("hello world")
print("I like 6.00.1x!")
x =1
if x !=1:
    print('yay')
else:
    print('hello world')

num = 5
if num > 2:
    print(num)
    num -=1
print(num)

n=1
while (n<11):
    print (n)
    n+1
    break
print("Goodbye!")

happy=3
if happy > 2:
    print('hello world')
    
varA = 1
varB = 2
if type(varA) == str or type(varB) == str:
    print('string involved')
else:
    if varA > varB:
        print("bigger")
    elif varA == varB:
        print("equal")
    else:
        print("smaller")
num = 5
if num > 2:
    print(num)
    num -= 1
print(num)

n=2
while (n<12):
    print(n)
    n=n+2
print("Goodbye")

end=7
n=1
mysum=0
while (n<end+1):
    mysum += n
    n=n+1
print (mysum)

for n in range (2,12,2):
    print(n)
print ("Goodbye!")

print("Hello!")
for n in range (10,0,-2):
    print(n)

n=1
end=6
mysum=0
for n in range(1,end+1):
    mysum +=n
    n=n+1
print (mysum)

cube = 9
for guess in range(abs(cube)+1):
    if guess**3 >= abs(cube):
        break
    if guess**3 != abs(cube):
        print (cube, 'is not a perfect cube')
    else:
        if cube < 0:
            guess = -guess
        print ('Cube root of ' + str(cube) + ' is ' + str(guess))
s = 'azcbobobegghakl'
count=0
for letter in s:
    if letter == 'a', or 'e''i''o' or 'u':
        count +=1
        print(count)