#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 07:22:06 2022

@author: noahjohnson
"""

import requests as rq
import numpy as np

f = rq.get("https://raw.githubusercontent.com/njohnso8/relevant-work/main/Advent%20of%20Code/Input/day7.txt")
f = f.text

#pre-processing
f = f.split("\n$")
f[0] = f[0].split("$")[1]

f = [f[i].split("\n") for i in range(len(f))]
f[-1] = f[-1][0:(len(f[-1]) - 1)]

size_dict = {}
curr_path = []
numstring = "1234567890"

##get file sizes out 
for i in range(len(f)):
    if ".." in f[i][0]:
        curr_path.remove(curr_path[-1])
    elif "cd" in f[i][0]:
        curr_path.append(f[i][0].split(" cd ")[1])
    
    if tuple(curr_path) not in list(size_dict.keys()):
        size_dict[tuple(curr_path)] = 0
        
    if (len(f[i]) > 1):       
        for j in range(1, len(f[i])):
            first_part = f[i][j].split(" ")[0]
            if first_part != "dir":
                size_dict[tuple(curr_path)] += int(first_part)
            
##get all values into higher dirs
keys_list = list(size_dict.keys())
values_list = list(size_dict.values())
for m in range(1, len(keys_list)):
    curr_key = keys_list[m]
    curr_value = values_list[m]
    for n in range(m):
        comp_key = keys_list[n]
        if keys_list[n] == curr_key[0:len(keys_list[n])]:
            values_list[n] += curr_value


size_dict_new = dict(zip(keys_list, values_list))

##get size under 100,000
size_dict_under = {k : v for (k, v) in size_dict_new.items() if v <= 100000}
np.sum(list(size_dict_under.values()))

##part 2
total_disk_space = 70000000
unused_space = total_disk_space - size_dict_new[('/',)]
needed_space = 30000000 - unused_space

size_dict_more_than_needed = {k : v for (k, v) in size_dict_new.items() if v >= needed_space}      

##get where it's located and what size it is
smallest_dir_ind = min(list(size_dict_more_than_needed.values()))  
smallest_dir_ind 
smallest_dir = list(size_dict_new.keys())[list(size_dict_new.values()).index(smallest_dir_ind)]
smallest_dir
