#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 08:43:00 2022

@author: noahjohnson
"""

import requests as rq

f = rq.get("https://raw.githubusercontent.com/njohnso8/relevant-work/main/Advent%20of%20Code/Input/day12.txt")
f = f.text
where_s = f.index("S")
where_e = f.index("E")
f = f.split("\n")
f = [list(f[i]) for i in range(len(f))]
get_row_s = where_s // 61
get_col_s = where_s % 62
get_row_e = where_e // 61
get_col_e = where_e % 62
f = f[0:(len(f) - 1)]
f[get_row_s][get_col_s] = "a"
f[get_row_e][get_col_e] = "z"


path_list = [f[get_row_s][get_col_s]]
path_list[0] += "#"
options = [(get_row_s + 1, get_col_s), (get_row_s - 1, get_col_s), \
           (get_row_s, get_col_s + 1)]
options = [x for x in options if ord(f[x[0]][x[1]]) <= ord(path_list[0][0]) + 1]
options_vals = [f[x[0]][x[1]] for x in options]
options_vals = sorted(options_vals, reverse = True)
min_path = 3000

while (not "*") in options_vals:
    choice = options[["#" not in i for i in options_vals].index(True)]
    choice_x = choice[0]
    choice_y = choice[1]
    f[choice_x][choice_y] += "#"
    options = []
    options = [(choice_x + 1, choice_y), (choice_x - 1, choice_y), \
               (choice_x, choice_y + 1), (choice_x, choice_y - 1)]
        
    options = [x for x in options if (ord(f[x[0]][x[1]]) <= ord(path_list[0][0]) + 1) and ]
    
    #insert tree search here