#!python3
#6.7实践代码

tableData=[['apples','oranges','cherries','bannae'],
           ['Alice','Bob','calo','David'],
           ['ge','ning','moose','goose']]
table=[['ge','ning'],
       ['li','lei']]

import pyperclip

colWidths=[0]*len(tableData)

def printTable(tableData):
    max=0
    for x in range(len(tableData[0])):
        for y in range(len(tableData)):
            if max>len(tableData[y][x]):
                max=max
            else:
                max=len(tableData[y][x])
    print('max:'+ str(max))

    for x in range(len(tableData[0])):
        for y in range(len(tableData)):
            if y==len(tableData)-1:
                dot='\n'
            else:
                dot=' '
            print(tableData[y][x].rjust(max),end=dot)

printTable(table)
