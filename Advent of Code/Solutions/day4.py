#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 08:13:23 2022

@author: noahjohnson
"""

import requests as rq

f = rq.get("https://raw.githubusercontent.com/njohnso8/relevant-work/main/Advent%20of%20Code/Input/day4.txt")
f = f.text
f = f.split("\n")
f = f[0:(len(f) - 1)]

cont_count = 0
overlap_count = 0
for i in range(len(f)):
    two_ranges = f[i].split(",")
    first_n1 = int(two_ranges[0].split("-")[0])
    first_n2 = int(two_ranges[0].split("-")[1])
    second_n1 = int(two_ranges[1].split("-")[0])
    second_n2 = int(two_ranges[1].split("-")[1])
    
    #part 1
    isfirst = (first_n2 - first_n1) >= (second_n2 - second_n1)

    if isfirst and second_n1 >= first_n1 and second_n2 <= first_n2:
        cont_count += 1
    
    elif not isfirst and first_n1 >= second_n1 and first_n2 <= second_n2:
        cont_count += 1
        
    #part 2
    ishigher = first_n2 >= second_n2
    if ishigher and second_n2 >= first_n1:
        overlap_count += 1
    elif not ishigher and first_n2 >= second_n1:
        overlap_count += 1
    
    
print(cont_count)
print(overlap_count)       