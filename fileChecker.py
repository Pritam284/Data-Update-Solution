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
import datetime
import shutil
import sys

sys.dont_write_bytecode = True


# Define checkFiles() function to detemine whether file exists or not

def checkFiles(rawFileLocation,inputFileLocation,dateSuffix):
	# Introduce source location - (Provide exact file name if possible, or create a function to find the file)
	fileDirList = [
					# Daily files - convert if necessary
					['PRS','PRS1_'],
					['PRS','PRS2_'],
					['PRS','PRS3_']
					]
	pathSep = '/'
	# Introduce a file counter to check on total file number
	fileCounter = 0
	# Loop through the list and check for the files -
	print('\nTrying to copy necessary files.\n', end='\n')
	for vendorDir in fileDirList:
		# Introduce source file's full path with file extension
		srcFolder = rawFileLocation + pathSep + vendorDir[0] + pathSep
		srcFileName = vendorDir[1] + dateSuffix  + '.csv'
		fileSrcPath =  srcFolder + srcFileName
		if os.path.isfile(fileSrcPath) and os.path.exists(fileSrcPath):
			shutil.copy2(fileSrcPath,inputFileLocation)
			print('> {} - {} -> exists -> copied'.format(vendorDir[0], srcFileName), end='\n')
			fileCounter += 1
		else:
			print('* {} - {} -> does not exists'.format(vendorDir[0], srcFileName), end='\n')
			continue
	if fileCounter == len(fileDirList):
		print('\nAll files exists for - {}'.format(dateSuffix), end='\n')
		return 1
	else:
		print('\nTotal - {} of {} files exists for - {}'.format(fileCounter, len(fileDirList), dateSuffix), end='\n')
		return 0
# ---------------------------------------------------------------------------------------------------
# This is the standard boilerplate that calls the main() function
if __name__ == '__main__':
	main()
