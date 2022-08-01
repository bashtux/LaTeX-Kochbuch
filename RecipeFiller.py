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
#import pprint
import re
# ---------------------------------------------------------------------------

templateFile = 'TemplateFiller.tex'

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
    res =[]
    with open(templateFile) as infile:
        for line in infile:
            out = re.findall(r'(<\+.*?\+>)', line)
            if out != []:
                res.extend(out)
    return res



# ---------------------------------------------------------------------------
# Start interactive mode
# ---------------------------------------------------------------------------

print(bigRule)
centerText("test")

exit()

