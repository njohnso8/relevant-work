#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 17:28:02 2022

@author: noahjohnson
"""

import requests as rq
import numpy as np
f = rq.get("https://raw.githubusercontent.com/njohnso8/relevant-work/main/Advent%20of%20Code/Input/day10.txt")
f = f.text
f = f.split("\n")
f = f[0:(len(f) - 1)]
inst = [f[i].split(" ")[0] for i in range(len(f))]
num = [int(f[i].split(" ")[1]) for i in range(len(f)) if "a" in f[i]]

num_cycles = 2 * inst.count("addx") + inst.count("noop")
reg_val = 1
counter_on_inst = 0
counter_on_num = 0
index = 0
sig_scores_by_cycle = []
sprite_pos = np.array([0, 1, 2])
result_str = ""
for j in range(num_cycles):
    sig_scores_by_cycle.append((j + 1) * reg_val)
    curr_crt = j % 40
    counter_on_inst += 1
    if inst[index] == "addx" and counter_on_inst == 2:
        reg_val += num[counter_on_num]
        sprite_pos += num[counter_on_num]
        counter_on_num += 1
    if inst[index] != "addx" or counter_on_inst != 1:
        counter_on_inst = 0
        index += 1
    
    if curr_crt in sprite_pos:
        result_str += "#"
    else:
        result_str += "."
    
    if (j + 1) % 40 == 0:
        result_str += "\n"
    

total_sig_score = 0
for k in range(19, len(sig_scores_by_cycle) - 2, 40):
    total_sig_score += sig_scores_by_cycle[k]

print(total_sig_score)

#part 2
print(result_str)
    
    
    

