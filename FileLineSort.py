#!/usr/bin/env python
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  : Samuel Troxler
# Created Date: 2022/07/26
# version ='1.0'
# ---------------------------------------------------------------------------
""" Takes a prepared .tex file and sorts given sections of \input lines alphabetically.
    Sections need to start with %--BEGIN-- and end with %--END--
    The rest of the file will be copied, all output is written to temp.tex
"""
# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------
import sys
import os
import pprint
# ---------------------------------------------------------------------------

startMatch= '%--BEGIN--'
endMatch = '%--END--'
lineMatch = '\input'

status = 0
sortData = []


# ---------------------------------------------------------------------------
def writeLines(outFile, lineData):
    with open(outFile, "a") as outF:
        for line in lineData:
            outF.write(line)
#            outF.close()
# ---------------------------------------------------------------------------

if len(sys.argv) < 2:
    print("No file specified.")
    print("Ending")
    exit()

filename = sys.argv[1]

with open(filename, 'r') as data:
    for line in data:
        if endMatch in line:
            print("Stopping")
            status = 0
            if len(sortData) > 2:
                # depending on folder structure increase index
                sortData.sort(key = lambda x: x.split('/')[1])
            pprint.pprint(sortData)
            sortData.insert(0, "%--BEGIN--\n")
            pprint.pprint(sortData)
            writeLines("temp.tex", sortData)
            sortData = []

        if startMatch in line:
            print("Found it")
            status = 1

        if (lineMatch in line) and (status == 1):
            sortData.append(line)

        if status == 0:
            writeLines("temp.tex", line)
data.close()

os.remove(filename)
os.rename('temp.tex', filename)
