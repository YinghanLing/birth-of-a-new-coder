#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 13:26:02 2018

@author: lingyinghan
"""
#
#s='azcbobobegghaklbob'
##s='nahowbieroibohoe'
##s='bob'
##s=''
#w="bob"
#i = 0
#count =0
#while i < len(s)-2:
#    if s[i] == 'b' and s[i+1]=='o' and s[i+2]=='b':
#        count+=1
#    i+=1
#print(count)

s='bob'
w='bob'
i=0
count=0
for i in range(0, len(s)-len(w)+1):
    if s[i: i+len(w)] == w:
        count+=1
print(count)