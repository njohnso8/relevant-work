#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 19:48:06 2022

@author: noahjohnson
"""

import requests as rq
import math
#f = rq.get("https://raw.githubusercontent.com/njohnso8/relevant-work/main/Advent%20of%20Code/Input/day11.txt")
#f = f.text
f = "Monkey 0:\nStarting items: 79, 98\nOperation: new = old * 19\nTest: divisible by 23\nIf true: throw to monkey 2\nIf false: throw to monkey 3\n\
\nMonkey 1:\nStarting items: 54, 65, 75, 74\nOperation: new = old + 6\nTest: divisible by 19\nIf true: throw to monkey 2\nIf false: throw to monkey 0\n\
\nMonkey 2:\nStarting items: 79, 60, 97\nOperation: new = old * old\nTest: divisible by 13\nIf true: throw to monkey 1\nIf false: throw to monkey 3\n\
\nMonkey 3:\nStarting items: 74\nOperation: new = old + 3\nTest: divisible by 17\nIf true: throw to monkey 0\nIf false: throw to monkey 1\n"
f = f.split("\n")
f = [f[i].lstrip() for i in range(len(f)) if (i % 7 != 0 and i % 7 != 6)]
items = [f[i].split(": ")[1].split(", ") for i in range(len(f)) if "S" in f[i]]
#max_item = max([int(items[i][j]) for i in range(len(items)) for j in range(len(items[i]))])
for m in range(len(items)):
    for n in range(len(items[m])):
        items[m][n] = int(items[m][n]) #/ max_item

ops = [f[i].split(": ")[1].split(" = old ")[1] for i in range(len(f)) if "O" in f[i]]
test = [int(f[i].split(" by ")[1]) for i in range(len(f)) if "T" in f[i]]
true_list = [int(f[i].split(" monkey ")[1]) for i in range(len(f)) if "true" in f[i]]
false_list = [int(f[i].split(" monkey ")[1]) for i in range(len(f)) if "false" in f[i]]

num_cycles = 10000
monkey_inspect = {p : 0 for p in range(8)}
for i in range(num_cycles):
    for j in range(len(items)):
        for k in range(len(items[j])):
            #j = 3
            worry_score = items[j][0]
            op_elements = ops[j].split(" ")
            if op_elements[1] == "old":
                op_elements[1] = worry_score
                
            if op_elements[0] == "*":
                worry_score = (worry_score * int(op_elements[1])) #// 3
            elif op_elements[0] == "+":
                worry_score = (worry_score + int(op_elements[1])) #// 3
            
            items[j].remove(items[j][0])
            if worry_score % test[j] == 0:
                items[true_list[j]].append(worry_score % math.prod(test))
            else:
                items[false_list[j]].append(worry_score % math.prod(test))
            
            monkey_inspect[j] += 1

monkey_list = sorted(monkey_inspect.values(), reverse = True)
print(monkey_list[0] * monkey_list[1])

            
    