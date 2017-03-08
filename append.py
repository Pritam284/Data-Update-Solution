#!/usr/bin/python -tt

# Author: Pritam Das
# Copy Right: Pritam Das 
# License: Under GPU License
# Restriction: Proprietary information can't be removed
# For more information: www.pysource.org/privacy
# ---------------------------------------------------------------------------------------------------
# Python Interpreter: 3.4.1
# ---------------------------------------------------------------------------------------------------
import csv
import csv as csv
import os
import shutil
import xlrd
import re
from datetime import datetime, date, time, timedelta
import time

file1="PRS1_20160330.csv" 
file2="PRS2_20160330.csv" 
file3="PRS3_20160330.csv" 

with open("final.csv","a") as fout:
    # first file:
    print("\n---->Initializing Append Program..........<----\n",end='\n')
    with open(file1) as f:
        # Copy & write including Header File
        for line in f:
            fout.write(line)

    print("\n-> [ Appended First File ]\n",end='\n')
    with open(file2) as f:
        next(f)
        # "next" will skip the header of the 2nd file
        for line in f:
          fout.write(line)

    print("\n-> [ Appended Second File ]\n",end='\n')
    with open(file3) as f:
        next(f)
        # "next" will skip the header of the 3rd file
        for line in f:
          fout.write(line)
    print("\n-> [ Appended Third File ]\n",end='\n')
    print("\n-> ***** Successfully Executed Append Operation *****\n",end='\n')
