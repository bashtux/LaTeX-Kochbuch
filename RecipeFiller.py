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
import fileinput
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

#def writeLines(outFile, lineData):
#    with open(outFile, "a") as outF:
#        for line in lineData:
#            outF.write(line)

#def replaceTags():
#    with open(r'test.tex', 'r') as file:
#        data = file.read()
#        data = data.replace('<+recipename+>', 'Pommes')
#
#    with open(r'out.tex', 'w') as file:
#        file.write(data)

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

def validate(text, options):
    while True:
        inp = input(text)
        if (inp.upper() in (string for string in options)):
            i = options.index(inp.upper())
            res = options[i]
            break
        else:
            print("Enter a valid option")
    return res

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
names["<+portion+>"] = validate("Define if the amount is Portions [P] or Pieces [S]: ", ['P', 'S'])
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
        ch = get_key(int(d), dietary)
        names["<+dietary+>"] = ch.replace(" ", "").lower()
        break
    else:
        print("Please enter a valid choice.")
print(smallRule)

#.......................................
spice = validate("Choose a spice level [0-4]: ", ["0", "1", "2", "3", "4"])
names["<+spicy+>"] = "S" + spice
print(smallRule)


# ---------------------------------------------------------------------------
# Ingredient list generator

listname = []
ingredientlist = []

s = validate("Use single list (named ingredients)[S] or \n use multiple sub lists (induvidually named) [M] :", ['S', 'M'])

# Start single or multi list environment

# Single list
if s == 'S':
    listname.append('Ingredients')
    c = 'Y'
    ingredientlist.append([])
    while c == 'Y':
        amnt = input("Amount: ")
        unit = input("Unit: ")
        name = input("Ingredient: ")
        ingredientlist[0].append([amnt, unit, name])
        next = input("Add another ingredient?")
        if next == 'N':
            break

if s == 'M':
    listName = 'C'
    ingredientlist.append([])
    cnt = 0
    while listName == 'C':
        c = 'Y'
        listname.append(input("List name: "))
        while c == 'Y':
            amnt = input("Amount: ")
            unit = input("Unit: ")
            name = input("Ingredient: ")
            ingredientlist[cnt].append([amnt, unit, name])
            next = input("Add another ingredient?")
            if next == 'N':
                break
        next = input("Add another list?")
        if next == 'N':
            break
        cnt = cnt + 1
        ingredientlist.append([])

# ---------------------------------------------------------------------------
# adding Steps to recipe

steps = []

while True:
    steps.append(input("Add step description:"))
    if validate("Add another step? ", ['Y', 'N']) == 'N':
        break


# ---------------------------------------------------------------------------
# Create recipe template
# ---------------------------------------------------------------------------
del names["<+steps+>"]
del names["<+ingredients+>"]

recipename = names["<+recipename+>"].lower() + "_" + names["<+subtitle+>"]

fin = open("test.tex", "rt")
data = fin.read()

# ---------------------------------------------------------------------------
# write general data into file
for word, replacement in names.items():
    data = data.replace(word, replacement)

# ---------------------------------------------------------------------------
# write ingredient list data
listNr = 0
allIngredients = ""
for n in listname:
    allIngredients += "\t\inglist[" + n + "]\n"
    cnt = 0
    for m in ingredientlist[listNr]:
        allIngredients += (
                "\t\t\ingredient{" +
                m[0] +
                "}{" +
                m[1] +
                "}{" +
                m[2] +
                "}\n" )
        cnt += 1
    listNr += 1
data = data.replace("<+ingredients+>", allIngredients)

# ---------------------------------------------------------------------------
# write steps to data
allSteps = ""
for n in steps:
    allSteps += "\t\steps{" + n + "}\n"
    print(n)
data = data.replace("<+steps+>", allSteps)

fin.close()
fin = open(recipename + ".tex", "wt")
fin.write(data)
fin.close()

#pprint.pprint(steps)

#    pprint.pprint(listname)
#    pprint.pprint(ingredientlist)

#print("\n\nList1")
#pprint.pprint(ingredientlist[0])
#print("\n\nList2")
#pprint.pprint(ingredientlist[1])

#pprint.pprint(names)

exit()

