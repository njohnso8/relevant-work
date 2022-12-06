#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 21:47:21 2022

@author: noahjohnson
"""

f = open("/Users/noahjohnson/Downloads/relevant-work/Advent of Code/day3.txt")
f = f.read().split("\n")
f = f[0:(len(f) - 1)]

#part 1
sum_rs = 0
for i in range(len(f)):
    rs = f[i]
    start_second = (len(rs) // 2)
    first_half = rs[0:start_second]
    second_half = rs[start_second:]
    found = False
    count = 0
    while not found:
        if first_half[count] in second_half:
            found = True
        count += 1
    doc_char = first_half[count - 1]
    
    if doc_char.isupper():
        value = ord(doc_char) - 64 + 26 
    else:
        value = ord(doc_char) - 96
        
    if i < 5:
        print(value)
        print(doc_char)
    
    sum_rs += value

print(sum_rs)

#part 2
sum_rs_group = 0
for i in range(len(f) // 3):
    rs_group = [f[3 * i], f[3 * i + 1], f[3 * i + 2]]
    candidates = []
    for j in range(len(rs_group[0])):
        if rs_group[0][j] in rs_group[1]:
            candidates.append(rs_group[0][j])
    found = False
    cand_count = 0
    while not found:
        if candidates[cand_count] in rs_group[2]:
            found = True
        cand_count += 1
    
    doc_char = candidates[cand_count - 1]
    
    if doc_char.isupper():
        value = ord(doc_char) - 64 + 26 
    else:
        value = ord(doc_char) - 96
    
    sum_rs_group += value

print(sum_rs_group)
        

    