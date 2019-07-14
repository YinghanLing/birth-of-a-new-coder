#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 11:19:45 2019

@author: lingyinghan
"""
num=19
if num < 0:
    isNeg = True
    num = abs(num)
else:
    isNeg = False
    result = ''
if num == 0:
    result ='0'
while num >0:
    result = str(num%2) + result
    num = num//2
if isNeg:
    result= '-' + result