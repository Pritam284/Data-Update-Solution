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

import os
import csv
import re
import datetime
import shutil
import update2new
import sys

sys.dont_write_bytecode = True


# Define checkFiles() function to detemine whether file exists or not

def fileOp(inputFileLocation,outputFileLocation,dateSuffix):
            # Introduce source location - (Provide exact file name if possible, or create a function to find the file)
            fileDirList = [
                                            # Daily files - convert if necessary
                                            ['Input','PRS1_'],
                                            ['Input','PRS2_'],
                                            ['Input','PRS3_']
                                            ]
            pathSep = '/'
            # Introduce a file counter to check on total file number
            #fileCounter = 0
            # Loop through the list and check for the files -
            print('\nFinal Processing.\n', end='\n')
            for fileDir in fileDirList:
                    # Introduce source file's full path with file extension
                    srcFolder = inputFileLocation+pathSep 
                    srcFileName = fileDir[1] + dateSuffix  + '.csv'
                    print('\nFile name..[ {} ]'.format(srcFileName),end='\n')
                    fileSrcPath =  srcFolder + srcFileName
                    fname, ftype=srcFileName.rsplit('.',1)
                    fmain,fdate = fname.rsplit('_',1)

                    if fmain == 'PRS1':
                        src=update2new.updateToNew(fileSrcPath)
                        old_file = "D:/Pritam/Raw Data Process  v1.0"+pathSep+"lol.csv"
                        rename = outputFileLocation+pathSep+ 'PRS1_'+dateSuffix+'.csv'
                        os.rename(old_file,rename)
                        print('\nSuccessfully Executed [ {} ]......'.format(rename),end='\n')
                        continue
                                                
                    elif fmain == 'PRS2':
                        src=update2new.updateToNew(fileSrcPath)
                        old_file = "D:/Pritam/Raw Data Process  v1.0"+pathSep+"lol.csv" 
                        rename = outputFileLocation+pathSep+ 'PRS2_'+dateSuffix+'.csv'
                        os.rename(old_file,rename)
                        print('\nSuccessfully Executed [ {} ]......'.format(rename),end='\n')
                        continue
                        
                    elif fmain == "PRS3":
                        src=update2new.updateToNew(fileSrcPath)
                        old_file = "D:/Pritam/Raw Data Process  v1.0"+pathSep+"lol.csv"
                        rename = outputFileLocation+pathSep+ 'PRS3_'+dateSuffix+'.csv'
                        print('\nSuccessfully Executed [ {} ]......'.format(rename),end='\n')
                        os.rename(old_file,rename)
                        continue
           
            

# ---------------------------------------------------------------------------------------------------
# This is the standard boilerplate that calls the main() function
if __name__ == '__main__':
	main()
                        
                    
