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
import csv as csv
import os
import shutil
import xlrd
import re
from datetime import datetime, date, time, timedelta
import time
import sys

sys.dont_write_bytecode = True



def up(src_dest):
  
    #print("Hi")
    first_File=fileProcess(src_dest)
    destFile = columnToDel(first_File)
    
    os.remove('outfile.csv')
    os.remove('new.csv')
    os.remove('pp.csv')

    return destFile

def fileProcess(src):

    print('\nFetching Data From [ {} ] .....'.format(str(src)), end='\n')

    #Removing first 6 columns 
    FIRST_ROW_NUM=1
    ROWS_TO_DELETE = {1,2,3,4,5,6}

    with open(src,'r')as infile, open('outfile.csv', 'w') as outfile:
            outfile.writelines(row for row_num, row in enumerate(infile, FIRST_ROW_NUM)
                        if row_num not in ROWS_TO_DELETE)
	    		
    print('\n*******Processing Data....******',end='\n')

    #Removing NIL from the file
    with open("outfile.csv","r") as f, open ('new.csv','w') as out:
                data = f.read()
                new_data = re.sub("NIL"," ",data)
                data = new_data
                out.write(data)  
                         
    print("------->>> Deleting NIL..")


    customDate = (date.today()-timedelta(1)).strftime('%Y%m%d')

           
            

    #Removing Total from last row
    with open("new.csv","r") as f_origin, open ('pp.csv','w') as dest:
            for line in f_origin:
                       if not line.startswith('Total'):
                            dest.write(line)
    return dest
    
    

def columnToDel(f_file):
    delete = ["LAC", "RAC"]
    with open("pp.csv","r") as infile, open("lol.csv", "w",newline="") as outfile:
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
                dest = w.writerow(row)
   
            print("******DONE******")
            return dest
        
def updateToNew(srcFile):
    print('\n<------Initializing Updating Process For [ {} ]------>'.format(srcFile),end='\n')
    destFile=up(srcFile)
    return destFile
    
    #fileProcess()
    

	

# ---------------------------------------------------------------------------------------------------
# This is THE standard boilerplate that calls THE main() function
if __name__ == '__main__':
	main()
