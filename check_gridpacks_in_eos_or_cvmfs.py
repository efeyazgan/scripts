import os,sys
my_path = '/tmp/'+os.environ['USER']+'/replace_gridpacks/'

requests = [
'EXO-RunIISpring18wmLHEGS-00011',
'EXO-RunIISpring18wmLHEGS-00012',
'EXO-RunIISpring18wmLHEGS-00013',
'EXO-RunIISpring18wmLHEGS-00014',
'EXO-RunIISpring18wmLHEGS-00015',
           ]
path1 = '/cvmfs/cms.cern.ch/phys_generator'
path2 = '/eos/cms/store/group/phys_generator/cvmf'
print(path1)
print(path2)
##########################################
######## START LOOP OVER PREPIDS #########
##########################################
for prepid in requests:

        os.system('echo '+prepid)

        os.system('mkdir -p '+my_path+'/'+prepid)
        os.chdir(my_path+'/'+prepid)
        os.system('wget -q https://cms-pdmv.cern.ch/mcm/public/restapi/requests/get_fragment/'+prepid+' -O '+prepid)
        gridpack_cvmfs_path = os.popen('grep \/cvmfs '+prepid+'| grep -v \'#args\' ').read()
        gridpack_cvmfs_path = gridpack_cvmfs_path.split('\'')[1]
#       print type(gridpack_cvmfs_path)
        gridpack_eos_path = gridpack_cvmfs_path.replace("/cvmfs/cms.cern.ch/phys_generator","/eos/cms/store/group/phys_generator/cvmfs")
#       print (gridpack_eos_path)       
        print (gridpack_cvmfs_path)
#       os.system('tar xf '+gridpack_eos_path+' -C'+my_path+'/'+prepid)
        os.system('tar xf '+gridpack_cvmfs_path+' -C'+my_path+'/'+prepid)
        os.system('more '+my_path+'/'+prepid+'/'+'runcmsgrid.sh | grep "FORCE IT TO"')
        os.system('grep _CONDOR_SCRATCH_DIR '+my_path+'/'+prepid+'/'+'mgbasedir/Template/LO/SubProcesses/refine.sh')
        os.system('grep "= ickkw" '+my_path+'/'+prepid+'/'+'process/madevent/Cards/run_card.dat')
        os.system('echo "------------------------------------"')
        os.system('rm '+prepid)
##########################################
######## END LOOP OVER PREPIDS ###########
##########################################
