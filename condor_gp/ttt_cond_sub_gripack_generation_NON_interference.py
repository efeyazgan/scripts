import os,sys,time
import string
import re
import time
import subprocess
import glob
from subprocess import Popen

particle = "a0" #"a0" or "s0"

path = '/afs/cern.ch/user/e/efe/workspace_afs/GENprod12/genproductions/bin/MadGraph5_aMCatNLO/cards/production/2017/13TeV/g2HDM/'
#path = '/eos/cms/store/group/phys_generator/cvmfs/gridpacks/UL/13TeV/madgraph/V5_2.6.5/g2HDM/ttc/'
#files = os.listdir(path)
files = glob.glob("/afs/cern.ch/user/e/efe/workspace_afs/GENprod12/genproductions/bin/MadGraph5_aMCatNLO/cards/production/2017/13TeV/g2HDM/ttt_"+particle+"_M*_rho*")
bash_com = '#!/bin/sh'
cd_com = 'cd /afs/cern.ch/user/e/efe/workspace_afs/GENprod12/genproductions/bin/MadGraph5_aMCatNLO/'
eval_com = 'eval `scram runtime -sh`'
#########./gridpack_generation.sh g2HDM_ttc_a0_M350_s0_M300_rhotu00_rhotc10_rhott00 cards/production/2017/13TeV/g2HDM/'######
main_com = './gridpack_generation.sh'

for file in files: 
    fname = file.split("/")[16]
    a0_mass = int(fname.split("_")[2].replace("M",""))
    print(fname,a0_mass)
    fw = open(fname+'_sub.sh','w')
    fw.write(bash_com+'\n')
    fw.write(cd_com+'\n')
    fw.write(main_com+' g2HDM_'+fname+' cards/production/2017/13TeV/g2HDM/'+fname+'\n') 
#    fw.write('mv g2HDM_'+fname+'*.tar.xz /eos/cms/store/group/phys_top/ExtraYukawa/tmp_gridpacks/.')
    print(fname)
    fw.write('mv g2HDM_'+fname+'*.tar.xz /eos/cms/store/group/phys_generator/cvmfs/gridpacks/UL/13TeV/madgraph/V5_2.6.5/g2HDM/ttt/.')
    fw.close()
    cond_submit_file = 'condor_submit_'+fname+'.sub'
    cond_submit = open(cond_submit_file,'w')
    sub_sh = fname+'_sub.sh'
    cond_submit.write('executable = '+sub_sh+'\n')
    cond_submit.write('universe   = vanilla'+'\n')
    cond_submit.write('output     = output_'+fname+'.out'+'\n')
    cond_submit.write('error      = error_'+fname+'.err'+'\n')
    cond_submit.write('log        = log_'+fname+'.log'+'\n') 
#   espresso     = 20 minutes
#   microcentury = 1 hour
#   longlunch    = 2 hours
#   workday      = 8 hours
#   tomorrow     = 1 day
#   testmatch    = 3 days
#   nextweek     = 1 week
    cond_submit.write('+JobFlavour= "tomorrow"'+'\n')
#   cond_submit.write('transfer_input_files = condor_get_cross_section_from_prepid_to_cmsrun_gridpack.py'+'\n')
#   cond_submit.write('transfer_output_files = '+file+'_log.txt'+'\n') 
    cond_submit.write('stream_output = True'+'\n')
#   cond_submit.write('should_transfer_files = YES'+'\n')
    cond_submit.write('queue')
    print("Submit file: "+cond_submit_file)
    print('condor_submit '+cond_submit_file)
    Popen(['chmod','755', sub_sh])
    Popen(['chmod','755',cond_submit_file])
    Popen(['condor_submit',cond_submit_file])
