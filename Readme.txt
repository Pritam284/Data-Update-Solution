**************Pritam's Tool v1.0***************

N.B. - This program will run on a pc with python environment only.

$$ How to Run -

--> Just double click on autorun.bat & it will start executing.
N.B. - Before starting the procedure delete _pycache_ folder from the directory. 

$$ Dependency - 

--> File's must be in csv format
--> File's should present at raw input location otherwise it won't work.
--> Raw input, Input & Output directory must be created & set the path on mainProgram.py 
--> It works only for a single day with e.g.day -1(Previous Day) feature. If needed to work for 3 days earlier then user 
    will have to change the PC date. Example - Processing file "PRS1_20160304" of Match 04 then PC date should be changed
    to March 05.

$$ Features - 

--> Check Files whether they are available in raw input location
--> If Files found it will copy files to input directory
--> Delete First 6 rows of a csv file   
--> Find "NIL" & replaced it with blank space
--> Delete LAC & RAC column from the csv files. 
--> Every csv file got Total with a number like (e.g.Total12165461) it will delete that row.
--> Then it will put the final output file's to output location directory. 

%------------Extensions ----------- %

append.py --> This program can append 3 files without taking headers from all the csv files. 

