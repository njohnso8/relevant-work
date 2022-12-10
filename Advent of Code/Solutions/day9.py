#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 09:11:37 2022

@author: noahjohnson
"""

import requests as rq
f = rq.get("https://raw.githubusercontent.com/njohnso8/relevant-work/main/Advent%20of%20Code/Input/day9.txt")
f = f.text

log_of_movement = [["*" for x in range(99)] for y in range(99)]
middle_ind = len(log_of_movement) // 2
log_of_movement[middle_ind][middle_ind] = "#"



log_of_movement_ts = "\n".join(["".join(log_of_movement[z]) for z in range(len(log_of_movement))])
log_of_movement_ts.count("#")