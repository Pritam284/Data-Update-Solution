#!/usr/bin/python -tt

# Author: Pritam Das
# Copy Right: Pritam Das 
# License: Under GPU License
# Restriction: Proprietary information can't be removed
# Email: pritam.acc@gmail.com
# Contact: +880-1673736945
# For more information: www.pysource.org/privacy
# ---------------------------------------------------------------------------------------------------
# Python Interpreter: 3.4.1
# ---------------------------------------------------------------------------------------------------

import csv
import sys

sys.dont_write_bytecode = True


def columnToDel(src):

    delete = ["LAC", "RAC"]
    with open(src) as infile, open("lol.csv", "w", newline="") as outfile:
  

            print("******Deleting LAC & RAC******")
            r = csv.DictReader(infile)
            # Need to read the first row so we know the fieldnames
            firstrow = next(r)  
            fields = r.fieldnames
           # Deleting LAC & RAC
            w = csv.DictWriter(outfile, 
                       [field for field in fields if not field in delete], 
                       extrasaction="ignore")
            w.writeheader()
            w.writerow(firstrow)
            for row in r:
                dest=w.writerow(row)
   
            print("******DONE******")
            return dest

