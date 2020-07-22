"""
This piece of code is meant to take the component content of a schematic and produce a library or expand on an existing library. This can be easily done due to KiCad depending primarily on .txt files.

"""
##miscellaneous imports
import os, shutil
import pandas as pd 
import numpy as np


print("Please enter the filepath and filename of \
    the schematic that you want to extract components/parts from.\
    The main file that you want is the file with no \
    extension. It should appear as <ProjectName> \
    along with the library files that carry the.lib, .dcm, and .bck \
    extensions. \n\n \
        PATH/<ProjectName> \
            library files \
        PATH/<ProjectName>.bck\
        PATH/<ProjectName>.dcm \
        PATH/<LibraryName>.lib")

print("This is your current working directory (cwd):\n\t", os.cwd())
sourcepath = input("project name/path (folder): ")
newlib_name = input("name of new library: ")
target_lib_location = input("path of where you want the library saved: ")

schem_partdata = sourcepath
    # copies to .txt user should delete later
shutil.copy2(schem_partdata, '{s}schem_partdata{n}.txt'.format(sourcepath, copy))    
        #rename to .txt file

os.chdir(sourcepath) #whatever the path is
folder_contents = os.listdir() 

for path, dirs, files in os.walk():
    print(files)

with open('prj_name.txt', 'r') as schemtext:

    data = rage.read().splitlines()
    headers = data[0].split(', ')
    for line in range(1, len(data)):
        data[line] = data[line].split('","')
    data = data[1:len(data)]
    df = pd.DataFrame(data, index = np.arange(1, len(data)+1), columns = headers)



## > truncates (clears file) | & | >> no truncate (does not celar)

