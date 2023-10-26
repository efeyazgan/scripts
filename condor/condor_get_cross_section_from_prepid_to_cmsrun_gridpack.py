#!/bin/env python
import os,sys,time,subprocess
import string
import re
import argparse
import textwrap

parser = argparse.ArgumentParser(
    formatter_class=argparse.RawDescriptionHelpFormatter,
    description=textwrap.dedent(''' help '''))
parser.add_argument('--file', type=str, help="gridpack filename", nargs='+')
parser.add_argument('--interference', type=int, help="interference A0/S0 or not", nargs='+')
args = parser.parse_args()

filen = ""

if args.file is not None:
    filen = args.file[0]
if args.interference is not None:
    is_interference = args.interference[0] 

if is_interference == 1:
    path = '/eos/cms/store/group/phys_generator/cvmfs/gridpacks/UL/13TeV/madgraph/V5_2.6.5/g2HDM/ttc_interference/'
else:
    path = '/eos/cms/store/group/phys_generator/cvmfs/gridpacks/UL/13TeV/madgraph/V5_2.6.5/g2HDM/ttc/'
#mainfolder = "/afs/cern.ch/user/e/efe/workspace_afs/testmgpythiawithcmssw/CMSSW_10_6_9/src"
mainfolder = "/afs/cern.ch/user/e/efe/workspace_afs/testmgpythiawithcmssw_12_4_8/CMSSW_12_4_8/src"


#fname = filen.split('_slc7')[0].split('g2HDM_ttc_')[1]
fname = filen.split('_el8')[0].split('g2HDM_ttc_')[1]
print(fname)
os.popen('rm -rf '+fname).read()
os.popen('mkdir '+fname).read()
os.popen('cp TOP-RunIISummer19UL17wmLHEGEN-00149_1_cfg.py '+fname+'/'+fname+'tmp_cfg.py').read()
fold = os.getcwd() + '/' + fname
fragment_file_tmp = fold +'/' + fname+'tmp_cfg.py'
fragment_file = fold +'/' + fname+'_cfg.py'
os.chdir(fold)
print(os.getcwd())
#print(fragment_file_tmp)
if os.path.isfile(fragment_file_tmp):
    f1 = open(fragment_file_tmp,"r+")
    f2 = open(fragment_file,"w")
    data_f1 = f1.read()
    data_f2 = data_f1.replace("g2HDM_ttc_a0_slc7_amd64_gcc700_CMSSW_10_6_0_tarball.tar.xz",filen)  #g2HDM_ttc_a0_slc7_amd64_gcc700_CMSSW_10_6_0_tarball.tar.xz
    data_f2 = data_f2.replace("/cvmfs/cms.cern.ch/phys_generator/","/eos/cms/store/group/phys_generator/cvmfs/") 
    print(data_f2)
    if is_interference == 1:
        data_f2 = data_f2.replace("g2HDM/ttc","g2HDM/ttc_interference")
    f1.close()
    f2.write(data_f2)    
    f2.close()
    os.popen('rm '+fragment_file_tmp).read()
    log_file = fold +'/' + fname+'_log.txt'
#    os.popen('scram b -j8').read()
    cmd = 'cmsRun -e -j test.xml '+fragment_file
    print(cmd)
    os.popen(cmd+' >& '+log_file).read()
#    os.popen('cp -n '+log_file+' '+mainfolder+'/.')
    os.popen('rm *.root *.xml')
