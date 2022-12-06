#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 07:24:14 2022

@author: noahjohnson
"""

import pandas as pd 
import requests as rq

f = rq.get("https://raw.githubusercontent.com/njohnso8/relevant-work/main/Advent%20of%20Code/Input/day6.txt")
f = f.text

def find_unique(f: str, n: int):
    c_list = list(f[0:n])
    unique_found = False
    count = n
    while not unique_found or count == len(f):
        num_unique = len(pd.unique(pd.Series(c_list)))
        if num_unique == n:
            unique_found = True
        else:
            c_list.remove(c_list[0])
            c_list.append(f[count])
            count += 1
            
    if count == len(f):
        return -1
    
    return count

if __name__ == "__main__":
    #part 1
    print("4 unique characters found at {0} characters.".format(find_unique(f, 4)))
    #part 2
    print("14 unique characters found at {0} characters.".format(find_unique(f, 14)))
