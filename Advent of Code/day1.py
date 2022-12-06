#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 20:14:38 2022

@author: noahjohnson
"""

import numpy as np
import requests as rq

f = rq.get("https://raw.githubusercontent.com/njohnso8/relevant-work/main/Advent%20of%20Code/day1.txt")
f = f.text
f = f.split("\n")

#part 1
max_count = 0
curr_count = 0
elf_count = 0
max_elf_count = 0
elf_counts = {}
print(f[-1])
for i in range(len(f)):
    
    if f[i] == "":
        elf_count += 1
        elf_counts[elf_count] = curr_count
        if curr_count > max_count:
            max_count = curr_count
            max_elf_count = elf_count
        curr_count = 0
            
    else:
        curr_count += int(f[i])

print("Elf #{0} had {1} calories".format(max_elf_count, max_count))

#part 2

elf_count_list = sorted(elf_counts.values(), reverse = True)
np.sum(elf_count_list[0:3])

