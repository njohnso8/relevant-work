#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 20:54:21 2022

@author: noahjohnson
"""

import requests as rq

f = rq.get("https://raw.githubusercontent.com/njohnso8/relevant-work/main/Advent%20of%20Code/Input/day2.txt")
f = f.text
f = f.split("\n")
f = f[0:len(f) - 1]

#part 1
sum_results = 0
for i in range(len(f)):
    raw_shape_val = ord(f[i][-1]) 
    shape_val = raw_shape_val - 87
    opp_shape_val = ord(f[i][0])
    match_val = (raw_shape_val - opp_shape_val) % 3
    if match_val == 0:
        result_val = 6
    elif match_val == 1:
        result_val = 0
    else: 
        result_val = 3
    
    total_val = shape_val + result_val
    sum_results += total_val
    
print("Strategy guide sum 1: {}".format(sum_results))

#part 2
sum_results_correct = 0
for i in range(len(f)):
    result_val = 3 * (ord(f[i][-1]) - 88)
    shape_val = ((ord(f[i][0]) + ((result_val - 3) // 3)) - 64)
    if shape_val == 0:
        shape_val = 3
    elif shape_val == 4:
        shape_val = 1
    total_val = result_val + shape_val
    sum_results_correct += total_val

print("Strategy guide sum 2: {}".format(sum_results_correct))
