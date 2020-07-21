"""
This piece of code is meant to take the component content of a schematic and produce a library or expand on an existing library. This can be easily done due to KiCad depending primarily on .txt files.

"""
##miscellaneous imports
import os
import shutil


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
orig_prj_name = input("project name/path: ")
newlib_name = input("name of new library: ")
# copy the file for safety, user should delete later
shutil.move(orig_prj_name, prj_name.txt)

os.chdir(prj_name.txt) #whatever the path is
folder_contents = os.listdir() 


### WITH STATEMENT ELIMINATES NEED FOR file.close() 

with open("prj_name.txt", r) as main_txt:
    data = file.readlines()
    o = open('newlib_name', 'w')
                """
                DO THE STUFFS HERE
                find the characters/sections to sep parts - '#'
                move that text elsewhere - new lib 
                """
    for line in data:
        line.replace('"', "")
        line.split(",")




## > truncates (clears file) | & | >> no truncate (does not celar)

