import os,sys,time
import string
import re
import time
import subprocess
from subprocess import Popen

path = '/eos/cms/store/group/phys_generator/cvmfs/gridpacks/UL/13TeV/madgraph/V5_2.6.5/g2HDM/ttc/'
files = os.listdir(path)
bash_com = '#!/bin/sh'
cd_com = 'cd /afs/cern.ch/user/e/efe/workspace_afs/testmgpythiawithcmssw/CMSSW_10_6_9/src'
eval_com = 'eval `scram runtime -sh`'
main_com = 'python condor_get_cross_section_from_prepid_to_cmsrun_gridpack.py --file'

counter = 0

for file in files:
    if counter > 20:
        continue
    if os.path.isfile(os.path.join(path, file)):
        if file.startswith('g2HDM'):
            fname = file.split('_slc7')[0].split('g2HDM_ttc_')[1]
            print(fname)
            if os.path.isdir(fname) is False:
                counter += 1
                fw = open(fname+'_sub.sh','w')
                fw.write(bash_com+'\n')
                fw.write(cd_com+'\n')
                fw.write(eval_com+'\n')
                fw.write(main_com+' '+file)
                fw.close()
                cond_submit_file = 'condor_submit_'+fname+'.sub'
                cond_submit = open(cond_submit_file,'w')
                sub_sh = fname+'_sub.sh'
                cond_submit.write('executable = '+sub_sh+'\n')
                cond_submit.write('universe   = vanilla'+'\n')
                cond_submit.write('output     = output_'+fname+'.out'+'\n')
                cond_submit.write('error      = error_'+fname+'.err'+'\n')
                cond_submit.write('log        = log_'+fname+'.log'+'\n') 
                cond_submit.write('transfer_input_files = condor_get_cross_section_from_prepid_to_cmsrun_gridpack.py'+'\n')
#                cond_submit.write('transfer_output_files = '+fname+'_log.txt'+'\n') 
                cond_submit.write('stream_output = True'+'\n')
#                cond_submit.write('should_transfer_files = YES'+'\n')
                cond_submit.write('queue')
                print("Submit file: "+cond_submit_file)
                print('condor_submit '+cond_submit_file)
                Popen(['chmod','755', sub_sh])
                Popen(['chmod','755',cond_submit_file])
                Popen(['condor_submit',cond_submit_file])
