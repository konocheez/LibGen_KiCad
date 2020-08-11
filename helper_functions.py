def add_fields (manuf, mpn, amanuf, ampn, pck):
    arbpos = ' 0 0 50 H I C CNN'
    field4 = 'F4 "{k}" {j}'.format(k=manuf, j=arbpos)
    field5 = 'F5 "{k}" {j}'.format(k=mpn, j=arbpos)
    field6 = 'F8 "{k}" {j}'.format(k=amanuf, j=arbpos)
    field7 = 'F7 "{k}" {j}'.format(k=ampn, j=arbpos)

    return field4, field5, field6, field7


def libadd (name, prt, pck, field0, field1, field2, field3, field4, field5, field6, 
field7):
# def libadd (name, prt, pck, *args, **kwargs):
    """
        name = definition
        prt = R/C (resistor or capacitor or polarized capacitor)
        pck = 0805/0603 (package)
        f0 = reference
        f1 = name/value
        f2 = footprint
        f3 = datasheet
        f4 = manufacturer
        f5 = mpn
        f6 = alt manufacturer
        f7 alt mpn
        """
    
    # for a in range(len(*args)):
    #     a = 'a{f}'.format

    partheader = '#\n# {k}\n#'.format(k=name)
    if prt == 'R':        #regular resistor
        DEF = 'DEF {k} R 0 0 N Y 1 F N'.format(k=name)
        f0 = 'F0 "{k}" 80 0 50 V V C CNN'.format(k=field0)
        f1 = 'F1 "{k}" 80 0 50 V V C CNN'.format(k=field1)
        f2 = 'F2 "{k}" 80 0 50 V V C CNN'.format(k=field2)
        f3 = 'F3 "{k}" 0 0 50 H I C CNN'.format(k=field3)

####### add in the other fields, and footer(footprint + drawing) ####

        f4, f5, f6, f7 = add_fields(field4, field5, field6, field7, pck)
        # partfooter = compdetails['res'][compdetails['res'].find('$FPLIST'): \
        #                     compdetails['res'].find('\n #')]
        index1 = compdetails['cp'].find('$ENDFPLIST')
        index2 = compdetails['cp'].find('\n #')
        fplst = '$FPLIST\n' + ' {k}_{j}*'.format(k=prt, j=pck)

        partfooter = '\n'.join([fplst, compdetails['cp'][index1:index2]])
        
    if prt == 'C':        #regular capacitor
        DEF = 'DEF {k} C 0 10 N Y 0 F N'.format(k=name)
        f0 = 'F0 "{k}" 25 100 50 H V L CNN'.format(k=field0)
        f1 = 'F1 "{k}" 25 -100 50 H V L CNN'.format(k=field1) 
        f2 = 'F2 "{k}" 38 -150 50 H I C CNN'.format(k=field2)
        f3 = 'F3 "{k}" 0 0 50 H I C CNN'.format(k=field3)

        f4, f5, f6, f7 = add_fields(field4, field5, field6, field7, pck)
        index1 = compdetails['cp'].find('$ENDFPLIST')
        index2 = compdetails['cp'].find('\n #')
        fplst = '$FPLIST\n' + ' {k}_{j}*'.format(k=prt, j=pck)

        partfooter = '\n'.join([fplst, compdetails['cp'][index1:index2]])        
        # partfooter = compdetails['c'][compdetails['c'].find('$FPLIST'): \
        #                     compdetails['c'].find('\n #')]

    if prt == 'CP':           #polarized capacitor
        DEF = 'DEF {k} C 0 10 N Y 1 F N'.format(k=name)
        f0 = 'F0 "{k}" 25 100 50 H V L CNN'.format(k=field0)
        f1 = 'F1 "{k}" 25 -100 50 H V L CNN'.format(k=field1)
        f2 = 'F2 "{k}" 38 -150 50 H I C CNN'.format(k=field2)
        f3 = 'F3 "{k}" 0 0 50 H I C CNN'.format(k=field3)
        
        f4, f5, f6, f7 = add_fields(field4, field5, field6, field7, pck)
        index1 = compdetails['cp'].find('$ENDFPLIST')
        index2 = compdetails['cp'].find('\n #')
        fplst = '$FPLIST\n' + ' {k}_{j}*'.format(k=prt, j=pck)

        partfooter = '\n'.join([fplst, compdetails['cp'][index1:index2]])+'\n'

    newprt = '\n'.join([partheader, DEF, f0, f1, f2, \
                f3, f4, f5, f6, f7, partfooter])

        
    return newprt
