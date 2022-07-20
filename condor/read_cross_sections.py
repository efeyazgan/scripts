import os,sys,time,subprocess
import string
import re

path = '/afs/cern.ch/user/e/efe/workspace_afs/testmgpythiawithcmssw/CMSSW_10_6_9/src/'
files = os.listdir(path)

fw = open('cross_section_table.txt','w')
fw.write("PID     Mass [GeV]   PID2  Mass2 [GeV]      rhotu    rhotc    rhott         cross-section [pb]       Err(cross-section) [pb]\n")
for file in files:
    if (file.startswith('a0') or file.startswith('s0')) and "sub" not in file and "M" in file:
        print("***** File = "+file)
        cs = os.popen('grep "After matching" '+file+'/*log.txt').read().replace("After matching: total cross section =","")
        print(cs)
#        cs = cs.replace("+-","$\pm$")
        cs = cs.replace("+-","              ")
        table_entries = file.split("_")
        print(table_entries)
        mass = ""
        mass2 = ""
        for ind in range(len(table_entries[1])):
            if ind == 0:
                continue
            mass += table_entries[1][ind]
        if file.startswith('a0') and 's0' in file:
            for ind in range(len(table_entries[3])):
                if ind == 0:
                    continue
                mass2 += table_entries[3][ind]
            tab = table_entries[0]+"      "+mass+"          "+table_entries[2]+"     "+mass2+"                  "+table_entries[4][5]+"."+table_entries[4][6]+"      "+table_entries[5][5]+"."+table_entries[5][6]+"      "+table_entries[6][5]+"."+table_entries[6][6]
        else:
            mass2 = "--"
            tab = table_entries[0]+"      "+mass+"          "+mass2+"                  "+table_entries[2][5]+"."+table_entries[2][6]+"      "+table_entries[3][5]+"."+table_entries[3][6]+"      "+table_entries[4][5]+"."+table_entries[4][6]
        table_row = tab+"          "+cs
        print(table_row)
        fw.write(table_row)
fw.close()
