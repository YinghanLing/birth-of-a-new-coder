#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 10:59:19 2018

@author: lingyinghan
"""

s = 'azcbobobegghakl'
count=0
for letter in s:
    if letter == 'a' or letter== 'e' or letter=='i' or letter=='o' or letter=='u':
        count +=1
print(count)

an_letters = "aefhilmnorsxAEFHILMNORSX"
word = input ("I will cheer for you! Enter a word: ")
times = int(input("Enthusiasm level (1-10):"))
i=0
while i < len(word):
    char = word [i]
    if char in an_letters:
        print("Give me an " + char + "!" + char)
    else:
        print ("Give me a " + char + "!" + char)
    i +=1
print ("What does that spell?")
for i in range (times):
    print (word, "!")