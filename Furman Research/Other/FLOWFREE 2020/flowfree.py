# -*- coding: utf-8 -*-
"""-
Created on Wed Dec 18 15:45:47 2019

@author: Caleb Roberson
"""


from __future__ import division
from graphics import *
from gurobipy import *
from math import *
import time
from time import sleep
import os
import sys
import csv
import xlsxwriter

from math import *

fieldRadius = 400
minRadius = 75
diskRadius = 5
numCircles = 0
currentVal = (fieldRadius * (math.pi / 2)) / 5
fairTerr = (fieldRadius * fieldRadius * math.pi) / 4
circleTerr = fairTerr - (minRadius * minRadius * (math.pi/4))

while(fieldRadius > minRadius):
    numCircles += math.floor(currentVal)
    currentVal += -1 * (math.pi / 2)
    fieldRadius += -1 * diskRadius
    
scalingFactor = math.floor(circleTerr/782.2312353192328)
answer = numCircles + scalingFactor
print(answer)

#store address for GLPK install to use in future commands
glpsol_addr = "C:\\glpk-4.65\\w64\\"
model_addr = "C:\\glpk-4.65\\w64\\flowfree\\"
#2020 command 
glpk_command = 'glpsol -m "' + model_addr + 'flowfree.txt" -d "' + model_addr + 'flowfreedata.txt" --wfreemps "' + model_addr + 'mps\\flowfreeresult3.mps" --check'
#glpk_command = 'glpsol -m "' + model_addr + '2019NECBLModel.txt" -d "' + model_addr + '2019NECBLData.txt" --wfreemps "' + model_addr + '2019NECBLpy.mps" --check'
print(glpk_command)



#call the operating system to run GLPK on the model and data files and create an mps file for gurobi to optimize
os.chdir(glpsol_addr)
os.system(glpk_command)
print(glpk_command)

#os.system("C:\glpk-4.55\w64\glpsol -m C:\Users\grannanbc\Dropbox\Backup\Grannan\NECBLModel -d C:\Users\grannanbc\Dropbox\Backup\Grannan\NECBLData --wfreemps C:\Users\grannanbc\Dropbox\Backup\Grannan\NECBL.mps --check")
m = read(model_addr + "mps\\flowfreeresult3.mps")
#m.Params.MIPFocus=1 
m.Params.presolve=2
#m.Params.Heuristics=0.4
#m.tune()
m.Params.MIPGap=0.01
#m.Params.VarBranch=1
#m.Params.TimeLimit=100000.0
start_time = time.time()
m.optimize()
status = m.status
if status == GRB.INFEASIBLE:
    print("INFEASIBLE")
    #m.computeIIS()
    #m.write("model.ilp")
    #sys.exit(0)
runTime = time.time() - start_time
print(runTime)
var_s = m.getVars()
#######################################
#print(var_s)
print('\n')
flowpath = {}
win = GraphWin('Floor', 500, 500)
win.setCoords(0.0, 0.0, math.sqrt(m.objVal), math.sqrt(m.objVal))
win.setBackground("black")
colorpaths = {'navy':[], 'DarkCyan':[], 'cyan':[], 'blue':[], 'salmon':[], 'magenta':[], 'white':[], 'gray':[], 'maroon':[], 'LimeGreen':[], 'red':[], 'ForestGreen':[], 'yellow2':[], 'orange':[], 'khaki2':[], 'DarkOrchid':[]}
for i in range(len(var_s)):
    if var_s[i].x == 1:
        name = var_s[i].getAttr('VarName')
        comma1 = name.find(',')
        comma2 = name[comma1 + 1:].find(',') + (comma1 + 1)
        x1 = int(name[2:comma1])
        y1 = int(name[comma1 + 1:comma2])
        point = (x1, y1)
        color = name[comma2 + 1: len(name) - 1]
        flowpath[point] = color
        rect = Rectangle(Point(y1 - 1, math.sqrt(m.objVal) - (x1 - 1)), Point(y1, math.sqrt(m.objVal) - x1))
        if color in colorpaths.keys():
            colorpaths[color].append(point)
        rect.draw(win)
        rect.setFill(color)
for key, value in colorpaths.items():
    if len(value) > 0:
        print("Path of " + key + " color: " + str(value) + '\n')
        print("The " + key + " color path has length: ", len(value) - 1)
        print('\n')
win.getMouse()
win.close()
        
# for i in range(len(var_s)):
#     if var_s[i].x == 1:
#         mindomset.append('('+var_s[i].varName[2:7]+')')
    # name = var_s[i].getAttr('VarName')
    # row = int(name[2])
    # column = int(name[4])
    # aisle = int(name[6])
    # if (row == 0 or row == 3) or (column == 0 or column == 5) or (aisle == 0 or aisle == 5):
    #     mindomset[var_s[i]] = 0
    # else:
    #     mindomset[var_s[i]] = 1
#print(mindomset)
        