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
import csvOperation
import fileChecker
import update2new
import sys

sys.dont_write_bytecode = True



def main():

                # Start the program execution clock
                program_start_time = time.time()
                human_readable_time = time.strftime("%H:%M:%S", time.localtime(program_start_time))
                print("\nProgram clock started at -> [ {} ]".format(str(human_readable_time)),end='\n')
                
                # Print an initialization message
                print("\n---->Initializing program..........<----\n",end='\n')

                dateSuffix = (date.today()-timedelta(1)).strftime('%Y%m%d') 

                inputFileLocation = 'D:/Pritam/PRS/Input'
                rawFileLocation= 'D:/Pritam/'
                outputFileLocation = 'D:/Pritam/PRS/Output/'
                
                # Check whether files are present or not, if present then copy them to input directory
                fileCheckStatus = fileChecker.checkFiles(rawFileLocation,inputFileLocation,dateSuffix)
                if fileCheckStatus == 1:
                        print("\n****** File Found ******", end='\n')
                        csvOperation.fileOp(inputFileLocation,outputFileLocation,dateSuffix)
                        
                else:
                        print('Files doesn\'t exists! Please upload the required files and try again later.')	# Print program execution time message

                program_elapsed_sec = (time.time() - program_start_time)
                program_elapsed_min = round((program_elapsed_sec / 60),2)
                print('\nProgram executed in [ {} ] minutes.'.format(program_elapsed_min), end='\n')

                # Print exit message
                print('***********Thanks For Using ME :-D************', end='\n')
                
                





# ---------------------------------------------------------------------------------------------------
# This is THE standard boilerplate that calls THE main() function
if __name__ == '__main__':
	main()
