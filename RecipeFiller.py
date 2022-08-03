#!/usr/bin/env python
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  : Samuel Troxler
# Created Date: 2022/07/27
# version ='1.0'
# ---------------------------------------------------------------------------
""" Interactive script to generate a recipe
"""
# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------
#import sys
#import os
import pprint
import re
# ---------------------------------------------------------------------------

templateFile = 'TemplateFiller.tex'
methods = {
        'Oven' : 'O',
        'Stove': 'S'
        }
dietary = {
        'None'          : 0,
        'Vegetarian'    : 1,
        'Vegan'         : 2,
        'Gluten free'   : 3,
        'Lactose free'  : 4 
        }

# ---------------------------------------------------------------------------
# Layouting
# ---------------------------------------------------------------------------
smallRule   = "-------------------------------------------------------------------------------"
bigRule     = "###############################################################################"




# ---------------------------------------------------------------------------
# Functions
# ---------------------------------------------------------------------------
def centerText(text):
    l = len(text)
    filler = int(((80-l)/2)+l)
    out = text.rjust(filler, " ")
    print(out)

def writeLines(outFile, lineData):
    with open(outFile, "a") as outF:
        for line in lineData:
            outF.write(line)

def replaceTags():
    with open(r'test.tex', 'r') as file:
        data = file.read()
        data = data.replace('<+recipename+>', 'Pommes')

    with open(r'out.tex', 'w') as file:
        file.write(data)

def searchTags(templateFile):
    res = {}
    with open(templateFile) as infile:
        for line in infile:
            out = re.findall(r'(<\+.*?\+>)', line)
            if out != []:
                for i in out:
                    res[i] = ""
    return res

def get_key(val, dict):
    for key, value in dict.items():
        if val == value:
            return key
 
    return "key doesn't exist"

# ---------------------------------------------------------------------------
# Start interactive mode
# ---------------------------------------------------------------------------

print(bigRule)
centerText("test")
print(bigRule)

#pprint.pprint(searchTags('TemplateFiller.tex'))
names = searchTags('TemplateFiller.tex')

#.......................................
names["<+recipename+>"] = input("Enter recipe name: ")
print(smallRule)

#.......................................
names["<+subtitle+>"] = input("Enter subtitle for recipe: ")
print(smallRule)

#.......................................
while True:
    port = input("Define if the amount is Portions [P] or Pieces [S]: ")
    if port.casefold() == 'P'.casefold():
        names["<+portion+>"] = 'P'        
        break
    elif port.casefold() == 'S'.casefold():
        names["<+portion+>"] = 'S'
        break
    else:
        print("Enter a valid choice.")
print(smallRule)

#.......................................
while True:
    n = input("Input amount recipe will produce: ")
    if n.isdigit():
        names["<+amount+>"] = n
        break
    else:
        print("Please enter a number.")
print(smallRule)

#.......................................
while True:
    at = input("Required active time for recipe [min]: ")
    if at.isdigit():
        names["<+activetime+>"] = at
        break
    else:
        print("Please enter a number.")
print(smallRule)

#.......................................
while True:
    pt = input("Total time for recipe [min]: ")
    if pt.isdigit():
        names["<+passivtime+>"] = pt
        break
    else:
        print("Please enter a number.")
print(smallRule)

#.......................................
for m, n in methods.items():
    print(m+"["+n+"]", end=", ")
print()
while True:
    m = input("Choose the cooking method: ")
    if m.casefold() == 'O'.casefold():
        names["<+methode+>"] = 'oven'
        break
    elif m.casefold() == 'S'.casefold():
        names["<+methode+>"] = 'stove'
        break
    else:
        print("Please enter a valid choice.")
print(smallRule)

#.......................................
for m, n in dietary.items():
    print(m+"["+str(n)+"]", end=", ")
print()

while True:
    d = input("Choose a dietary restriction: ")
    if d.isdigit() and int(d) < len(dietary):
        # .replace(" ", "").lower()
        ch = get_key(int(d), dietary)
        names["<+dietary+>"] = ch.replace(" ", "").lower()
        break
    else:
        print("Please enter a valid choice.")
print(smallRule)

#.......................................
while True:
    s = input("Choose a spice level [0-4]: ")
    if s.isdigit() and int(s) <= 4:
        names["<+spicy+>"] = "S" + s
        break
    else:
        print("Please enter a valid choice.")
print(smallRule)


# ---------------------------------------------------------------------------
# Ingredient list generator



pprint.pprint(names)

exit()

