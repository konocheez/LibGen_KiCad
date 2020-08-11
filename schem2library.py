"""
README

This piece of code is meant to take the Resistor and Capacitor components and content of a schematic and produce a KiCad library. This can be easily done due to KiCad depending primarily on text files. Only Resistors and Capacitors are accommodated in this code as that is what it was designed to remediate. There were a collection of schematics who only referenced the default "R-Device" and "C-Device" symbols, so those symbols are the basis for all components generated in this library

    name = definition
    prt = R/C (resistor or capacitor or polarized capacitor)
    pck = 0805/0603 (package)
    f0 = reference
    f1 = name/definition
    f2 = footprint
    f3 = datasheet
    f4 = manufacturer
    f5 = mpn
    f6 = alt manufacturer
    f7 = alt mpn
    
"""
##miscellaneous imports
import os, shutil
import pandas as pd 
import numpy as np
from helper_functions import libadd, add_fields

print("This is your current working directory (cwd):\n\t", os.getcwd())
print("Make sure that you ARE IN the desired directory or that you WILL MOVE the produced contents to your desired directory. The file used to generate this library will be the CSV file from the bom2csv script in the BOM Plugins of KiCad. This CSV contains valuable field information to generate the libary.")

#string variable initialization
mpn = "Manufacturer Part Number"
mpn_ = 'Manufacturer_Part_Number'
mpno = 'Manufacturer Part No.'
manuf = 'Manufacturer'
manuf_ = 'Manufacturer_Name'
ampn = 'Alt. Manufacturer Part Number'
amanuf = 'Alt. Manufacturer'
ref = 'Reference'
ds = 'Datasheet'
val = 'Value'
fp = 'Footprint'

csvfile = input("Enter the name of the csv file you'll be extracting from: ")

#reading the csvfile for dataframe organization/cleaning
with open(csvfile, 'r') as schemtxt:
    data = schemtxt.read().splitlines()
    headers = data[0].split(', ')       #headers need to be labeled headers
    for line in range(0, len(data)):
        data[line] = data[line].replace('","', ',,').strip('"')
        data[line] = data[line].split(',,')
        
    data = data[1:len(data)]
    #re-init data w/o headers

    df = pd.DataFrame(data, index = np.arange(1, len(data)+1), columns = headers)
    print("Let's see how the data is looking...\n", df.head(5))

# join the similarly labeled columns and delete the extras

################################ PART NUMBER ################################
if mpno or mpn_ in df.columns.values:
    df['Part Number'] = df['Part Number'].str.cat(df[[mpno, mpn_]])
    df = df.drop([mpn_, mpno], axis=1)
    df = df.rename(columns = {'Part Number' : mpn})

################################ MANUFACTURER NAME ################################
#repeat of part numbers
# if (len(df.columns.values[4]) == 0):

if manuf_ in df.columns.values:
    df[manuf] = df[manuf].str.cat(df[manuf_])
    df = df.drop([manuf_], axis=1)

df = df.drop(['Description'], axis=1)
df[val] = df[val].str.replace(" ", "")
why = df[val]
df[amanuf] = ''
df[ampn] = ''

drawlib = input("Enter the name of the library file you'd like to generate your drawing and footprint text from: ")

with open(drawlib, 'r') as raw:
    raw = raw.read().split('ENDDEF\n')
    compdetails = dict()
    for item in raw:
        if 'R-Device' in item:                                      #resistor
            compdetails.update({'res' : item + 'ENDDEF\n\n'})
        
        if 'C-Device' in item:                                      #capacitor
            compdetails.update({'c' : item + 'ENDDEF\n\n'})

        if 'CP-Device' in item:                                     #polarized capacitor
            compdetails.update({'cp' : item + 'ENDDEF\n\n'})

        item = item + 'ENDDEF\n'+'\n'

#### extra types of capacitors
        # if 'C_Small' in item:
        #     compdetails.update({'csmall' : item})            
            #draw unpolarized cap
#         if 'CP_Small' in item:
#             compdetails.update({'cpsmall' : item})
#             ##draw small unpolarized cap
#         if 'CP1-Device' in item:
#             cpdraw_us = item
#             compdetails.update({'cp1' : item})
#             #draw us symbol capacitor
#         if 'CP1_Small' in item:
#             compdetails.update({'cp1small' : item})

compdetails.update('C0805fp' : 'Capacitors_SMD:C_0805')
compdetails.update('R0805fp' : 'Resistors_SMD:R_0805')
compdetails.update('C0603fp' : 'Capacitors_SMD:C_0603')
compdetails.update('R0603fp' : 'Resistors_SMD:R_0603')
compdetails.update('C0402fp' : 'Capacitors_SMD:C_0402')
compdetails.update('R0402fp' : 'Resistors_SMD:R_0402')
compdetails.update('C1206fp' : 'Capacitors_SMD:C_1206')
compdetails.update('R1206fp' : 'Resistors_SMD:R_1206')
compdetails.update('C1210fp' : 'Capacitors_SMD:C_1210')

test = libadd('name', 'C', '0805', 'thing0', 'thing1', 'thing2', 'thing3', 'thing4', 'thing5', 'thing6', 'thing7')
print('if you see this, then it is working: \n', test)

mpn = '_6'
amanuf = '_7'
ampn = '_8'
val = "Value"

libfile = input("Enter the name of the library file you'd like to have generated: ")
with open(libfile, 'w') as libby:
    with open('ECG_MOUSE.lib', 'r') as ecg:
        initlines = ecg.readlines()
        print(initlines)
        libby.write(''.join(initlines[0:2]))
    for part in df.itertuples():
        # print(part)
        name = part.__getattribute__(val)
        f0 = part.__getattribute__(val)
        f1 = part.__getattribute__(ref)
        ptype = f1[0]
        f2 = part.__getattribute__(fp)
        f3 = part.__getattribute__(ds)
        f4 = part.__getattribute__(manuf)
        f5 = part.__getattribute__(mpn)
        f6 = part.__getattribute__(amanuf)
        f7 = part.__getattribute__(ampn)
        # print('hello', f5, f6, f7)
        # print(name, f0, f1, f2, f3, f4, f5)
        if '0805' in part.__getattribute__(fp):
            pck = '0805'
        elif '0603' in part.__getattribute__(fp):
            pck = '0603'
        elif '0402' in part.__getattribute__(fp):
            pck = '0402'
        elif '1206' in part.__getattribute__(fp):
            pck = '1206'
        elif '1210' in part.__getattribute__(fp):
            pck = '1210'

        if 'R' in f1[0] and 'RV' not in f1:
            libby.write(libadd(name, ptype, pck, f0, f1, f2, f3, f4, f5, f6, f7))
        if 'C' in f1[0]:
            libby.write(libadd(name, ptype, pck, f0, f1, f2, f3, f4, f5, f6, f7))
    libby.write('\n#\n#End Library')