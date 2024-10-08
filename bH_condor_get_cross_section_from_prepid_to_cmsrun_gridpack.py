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
parser.add_argument('--cgbh_arg',type=int, help="cgbh_new 1 or not",nargs='+')
#parser.add_argument('--interference', type=int, help="interference A0/S0 or not", nargs='+')
args = parser.parse_args()

filen = ""

if args.file is not None:
    filen = args.file[0]

if args.cgbh_arg is not None:
    cgbh_new = args.cgbh_arg[0]
if cgbh_new == 1:
    path = '/cvmfs/cms.cern.ch/phys_generator/gridpacks/slc7_amd64_gcc700/13TeV/madgraph/V5_2.6.5/cgbh-new/'
else:
    path = '/cvmfs/cms.cern.ch/phys_generator/gridpacks/UL/13TeV/madgraph/V5_2.6.5/g2HDM/cgbh/'
mainfolder = "/afs/cern.ch/user/e/efe/workspace_afs/testmgpythiawithcmssw_12_4_8/CMSSW_12_4_8/src"

fname = filen.split('_slc7')[0].split('cgbh_H_')[1]
print(fname)
os.popen('rm -rf '+fname).read()
os.popen('mkdir '+fname).read()
os.popen('cp TOP-RunIISummer20UL16wmLHEGENAPV-00616_1_cfg.py '+fname+'/'+fname+'tmp_cfg.py').read()
fold = os.getcwd() + '/' + fname
fragment_file_tmp = fold +'/' + fname+'tmp_cfg.py'
fragment_file = fold +'/' + fname+'_cfg.py'
os.chdir(fold)
print(os.getcwd())
if os.path.isfile(fragment_file_tmp):
    f1 = open(fragment_file_tmp,"r+")
    f2 = open(fragment_file,"w")
    data_f1 = f1.read()
    data_f2 = data_f1.replace("cgbh_H_M1000_rhott06_rhotc04_rhotu00_slc7_amd64_gcc10_CMSSW_12_4_8_tarball.tar.xz",filen)  #g2HDM_ttc_a0_slc7_amd64_gcc700_CMSSW_10_6_0_tarball.tar.xz
    if int(cgbh_new) != 1:
        data_f2 = data_f2.replace("slc7_amd64_gcc700/13TeV/madgraph/V5_2.6.5/cgbh-new","UL/13TeV/madgraph/V5_2.6.5/g2HDM/cgbh")
    data_f2 = data_f2.replace("/cvmfs/cms.cern.ch/phys_generator/","/eos/cms/store/group/phys_generator/cvmfs/")
    print(data_f2)
    f1.close()
    f2.write(data_f2)    
    f2.close()
    os.popen('rm '+fragment_file_tmp).read()
    log_file = fold +'/' + fname+'_log.txt'
    cmd = 'cmsRun -e -j test.xml '+fragment_file
    print(cmd)
    os.popen(cmd+' >& '+log_file).read()
    os.popen('rm *.root *.xml')
