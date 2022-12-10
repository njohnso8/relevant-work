#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 07:08:59 2022

@author: noahjohnson
"""

import requests as rq
import pandas as pd

f = rq.get("https://raw.githubusercontent.com/njohnso8/relevant-work/main/Advent%20of%20Code/Input/day8.txt")
f = f.text
f = f.split("\n")
f = f[0:(len(f) - 1)]
visible_ct = 2 * len(f[0]) + 2 * len(f) - 4 #perimeter of grid 
                                            #minus corners counted twice

dict_to_df = dict(zip(range(len(f)), f))
dict_to_df = {k : list(v) for k, v in dict_to_df.items()}
f = pd.DataFrame(dict_to_df)
f = f.transpose().astype(int)

#part 1

#count amount inside grid that are visible
for i in range(1, (len(f) - 1)):
    for j in range(1, (len(f) - 1)):
        curr_ht = f.iloc[i][j]
        #collection of all trees in each direction, to be considered
        all_left = f.iloc[i][0:j]
        all_right = f.iloc[i][(j + 1):len(f[i])]
        all_up = f.iloc[0:i][j]
        all_down = f.iloc[(i + 1):len(f)][j]
        #if taller than all trees in any direction, visible
        is_visible = (curr_ht > max(all_left)) or (curr_ht > max(all_right)) or \
            (curr_ht > max(all_up)) or (curr_ht > max(all_down))
        if is_visible:
            visible_ct += 1

print("There are {0} visible trees in this plot".format(visible_ct))

#part 2

def not_blocked(l, ref, direction):
    not_blocked = True
    if direction == "l" or direction == "u":
        start = len(l) - 1
        inc = -1
        edge = -1
    else:
        start = 0
        inc = 1
        edge = len(l)
    count = 0
    while not_blocked and start != edge:
        if l[start] >= ref:
            not_blocked = False
        else:
            start += inc
        count += 1
    return count 

max_ss = 0
for m in range(1, (len(f) - 1)):
    for n in range(1, (len(f) - 1)):
        curr_ht = f.iloc[m][n]
        all_left = list(f.iloc[m][0:n])
        all_right = list(f.iloc[m][(n + 1):len(f[m])])
        all_up = list(f.iloc[0:m][n])
        all_down = list(f.iloc[(m + 1):len(f)][n])
        left_score = not_blocked(all_left, curr_ht, "l")
        right_score = not_blocked(all_right, curr_ht, "r")
        up_score = not_blocked(all_up, curr_ht, "u")
        down_score = not_blocked(all_down, curr_ht, "d")
        ss = left_score * right_score * up_score * down_score
        if ss > max_ss:
            max_ss = ss

print("The maximum scenic score avaiable in this plot is {0}".format(max_ss))

