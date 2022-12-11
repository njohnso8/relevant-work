#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 09:11:37 2022

@author: noahjohnson
"""

import requests as rq
f = rq.get("https://raw.githubusercontent.com/njohnso8/relevant-work/main/Advent%20of%20Code/Input/day9.txt")
f = f.text
f = f.split("\n")
f = f[0:(len(f) - 1)]

log_of_movement = [["*" for x in range(999)] for y in range(999)]
middle_ind = len(log_of_movement) // 2
log_of_movement[middle_ind][middle_ind] = "#"

num_knots = 10
positions = [middle_ind for z in range(2 * num_knots)]

for i in range(len(f)):
    move = f[i].split(" ")
    direction = move[0]
    amt = int(move[1])
    if direction == "L" or direction == "U":
        amt *= -1
 
    for j in range(abs(amt)):
        step = amt // abs(amt)
        move_x = direction == "L" or direction == "R"
        move_y = direction == "U" or direction == "D"
        if move_x:
            positions[0] += step 
        elif move_y:
            positions[1] += step
        for k in range(num_knots - 1):
            diff_head_tail_x = positions[2 * k] - positions[2 * k + 2]
            dist_head_tail_x = int(abs(diff_head_tail_x))
            diff_head_tail_y = positions[2 * k + 1] - positions[2 * k + 3]
            dist_head_tail_y = int(abs(diff_head_tail_y))
        
            if dist_head_tail_x > 1 and dist_head_tail_y == 0:
                positions[2 * k + 2] += diff_head_tail_x // dist_head_tail_x
            elif dist_head_tail_y > 1 and dist_head_tail_x == 0:
                positions[2 * k + 3] += diff_head_tail_y // dist_head_tail_y
            elif dist_head_tail_x > 1 and dist_head_tail_y > 0:
                positions[2 * k + 2] += diff_head_tail_x // dist_head_tail_x
                positions[2 * k + 3] += 1 if diff_head_tail_y > 0 else -1
            elif dist_head_tail_y > 1 and dist_head_tail_x > 0:
                positions[2 * k + 3] += diff_head_tail_y // dist_head_tail_y
                positions[2 * k + 2] += 1 if diff_head_tail_x > 0 else -1
            
            #print(k, ":", positions)
            if k == num_knots - 2 and log_of_movement[positions[2 * k + 2]][positions[2 * k + 3]] == "*":
                log_of_movement[positions[2 * k + 2]][positions[2 * k + 3]] = "#"
    
log_of_movement_ts = "\n".join(["".join(log_of_movement[z]) for z in range(len(log_of_movement))])
log_of_movement_ts.count("#")



