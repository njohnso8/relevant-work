#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 12:34:27 2022

@author: noahjohnson
"""
import requests as rq

f = rq.get("https://raw.githubusercontent.com/njohnso8/relevant-work/main/Advent%20of%20Code/Input/day5.txt")
f = f.text
f = f.split("\n\n")
crates = f[0].split("\n")
instructions = f[1].split("\n")
instructions = instructions[0:(len(instructions) - 1)]
crate_list = [[],[],[],[],[],[],[],[],[]]
for i in range(len(crates[0]) // 4):
    for j in range(len(crate_list)):
        crate_list[j].append(crates[i][(4 * j):(4 * j + 3)])
        
for x in range(len(crate_list)): 
    crate_list[x] = [y for y in crate_list[x] if y != '   ']

for k in range(len(instructions)):
    curr = instructions[k]
    num_move = int(curr[curr.find(" "):curr.find(" ", curr.find(" ") + 1)])
    from_move = int(curr.split("from ")[1][0]) - 1
    to_move = int(curr.split("to ")[1][0]) - 1
    
    crates_moved = crate_list[from_move][0:num_move]
    #part 2 only
    crates_moved.reverse()
    
    for m in range(num_move):
        crate_list[to_move].insert(0, crates_moved[m])
        crate_list[from_move].remove(crates_moved[m])

for n in crate_list:
    print(n[0])
    
    
               
