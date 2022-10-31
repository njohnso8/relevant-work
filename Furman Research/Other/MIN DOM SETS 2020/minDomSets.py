# -*- coding: utf-8 -*-
"""-
Created on Wed Dec 18 15:45:47 2019

@author: Noah Johnson
"""


from __future__ import division
from gurobipy import *
import time
from time import sleep
import os
import sys
import csv
import xlsxwriter

#store address for GLPK install to use in future commands
dataString = "set Aisles := 1, 2, 3, 4, 5;"
extdataString = "set exAisles := 0, 1, 2, 3, 4, 5, 6;"
counter = 1
wb = xlsxwriter.Workbook('6x6x6_runtime.xlsx')
ws = wb.add_worksheet()
ws.write('A1', 'Graph')
ws.write('B1', '# Nodes')
ws.write('C1', 'Runtime (secs)')

for i in range(6, 7):
    if ';' in dataString:
        dataString = dataString.replace(';', ', ')

    if ';' in extdataString:
        extdataString = extdataString.replace(';', ', ')
        
    model_addr = "C:\\glpk-4.65\\w64\\mindomsets\\"
    
    with open(model_addr + "GLPKdomSetsdata.txt", 'r') as file:
        data = file.readlines()
        
    dataString += str(i) + ';'    
    data[4] = dataString + '\n'
    
    extdataString += str(i + 1) + ';'
    data[10] = extdataString
    
    with open(model_addr + "GLPKdomSetsdata.txt", 'w') as file:
        file.writelines(data)
    
    with open(model_addr + "GLPKdomSets.txt", 'r') as file1:
        model = file1.readlines()
        
    model[18] = "s.t. constraint3{i in Rows, j in Columns, k in {0, " + str(i + 1) + "}}: x[i, j, k] = 0;\n"
    
    with open(model_addr + "GLPKdomSets.txt", 'w') as file1:
        file1.writelines(model)
        
        
    glpsol_addr = "C:\\glpk-4.65\\w64\\"
    model_addr = "C:\\glpk-4.65\\w64\\mindomsets\\"
    #2020 command 
    glpk_command = 'glpsol -m "' + model_addr + 'GLPKdomSets.txt" -d "' + model_addr + 'GLPKdomSetsdata.txt" --wfreemps "' + model_addr + 'GLPKdomSetsresult.mps" --check'
    #glpk_command = 'glpsol -m "' + model_addr + '2019NECBLModel.txt" -d "' + model_addr + '2019NECBLData.txt" --wfreemps "' + model_addr + '2019NECBLpy.mps" --check'
    print(glpk_command)



#call the operating system to run GLPK on the model and data files and create an mps file for gurobi to optimize
    os.chdir(glpsol_addr)
    os.system(glpk_command)
    print(glpk_command)

#os.system("C:\glpk-4.55\w64\glpsol -m C:\Users\grannanbc\Dropbox\Backup\Grannan\NECBLModel -d C:\Users\grannanbc\Dropbox\Backup\Grannan\NECBLData --wfreemps C:\Users\grannanbc\Dropbox\Backup\Grannan\NECBL.mps --check")
    m = read(model_addr + "GLPKdomSetsresult.mps")
#m.Params.MIPFocus=1 
    m.ModelSense = 1
    
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
#print('\n')

    mindomset = []
    #matlab_str = ""
    rowlist = []
    collist = []
    aislelist = []
    

    for j in range(len(var_s)):
        if var_s[j].x == 1:
            name = var_s[j].getAttr('VarName')
            comma1 = name.find(',')
            comma2 = name[comma1 + 1:].find(',') + (comma1 + 1)
            row = int(name[2:comma1])
            if row not in rowlist:
                rowlist.append(row)
            column = int(name[comma1 + 1: comma2])
            if column not in collist:
                collist.append(column)
            aisle = int(name[comma2 + 1:len(name) - 1])
            if aisle not in aislelist:
                aislelist.append(aisle)
            #ws.write(counter, 0, row)
            #ws.write(counter, 1, column)
            #ws.write(counter, 2, aisle)
            #counter += 1
            mindomset.append((row, column, aisle))
            #matlab_str += str(row) + ' ' + str(column) + ' ' + str(aisle) + '; '
    #ws.write(counter, 0, "next dom set: " + str(len(rowlist)) + ' x ' + str(len(collist)) + ' x ' + str(len(aislelist) + 1))
    #wb.close()

#print("The minimum dominating set of a", len(rowlist), 'x', len(collist), 'x', len(aislelist), "grid graph is: \n", mindomset)
#print("\nThe domination number is: ", len(mindomset))
#print("\nThis is matlab input: \n", matlab_str)
    print(str(len(rowlist)) + ' x ' + str(len(collist)) + ' x ' + str(i) + " grid graph done")
    
    counter += 1
    ws.write('A'+str(counter), str(len(rowlist)) + ' x ' + str(len(collist)) + ' x ' + str(len(aislelist)))
    ws.write('B'+str(counter), len(rowlist)*len(collist)*i)
    ws.write('C'+str(counter), runTime)
    
    
    f = open('listOfDomSets_6x6x6.txt', 'a')
    f.write("The minimum dominating set of a " + str(len(rowlist)) + ' x ' + str(len(collist)) + ' x ' + str(len(aislelist)) + " grid graph is: \n" + str(mindomset))
    f.write("\nThe domination number is: " + str(len(mindomset)) + '\n' + '\n')
    f.close()

wb.close()
print("Done")


    
