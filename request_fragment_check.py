import os,sys,time,string
os.system('source /afs/cern.ch/cms/PPD/PdmV/tools/McM/getCookie.sh')
os.system('cern-get-sso-cookie -u https://cms-pdmv.cern.ch/mcm/ -o ~/private/prod-cookie.txt --krb --reprocess')
sys.path.append('/afs/cern.ch/cms/PPD/PdmV/tools/McM/')

from rest import McM
from json import dumps
from itertools import groupby

mcm = McM(dev=True)

#res = mcm.get('requests', query='prepid=TOP-RunIISummer15wmLHEGS-00023') # powheg
#res = mcm.get('requests', query='prepid=HIG-RunIIFall17wmLHEGS-01083') # no matching madgraph
res = mcm.get('requests', query='prepid=HIG-RunIISummer15wmLHEGS-02182') #fxfx

my_path =  '/tmp/'+os.environ['USER']+'/gridpacks/'

for r in res:
    pi = r['prepid']
    dn = r['dataset_name']
    print ("'"+r['prepid']+"',",r['dataset_name'])
    print (pi)
    os.system('wget -q https://cms-pdmv.cern.ch/mcm/public/restapi/requests/get_fragment/'+pi+' -O '+pi)
    os.system('mkdir -p '+my_path+'/'+pi)
    check = []
    ME = ["PowhegEmissionVeto","aMCatNLO"]
    MEname = ["powheg","madgraph","mcatnlo"]
    matching = 10
    ickkw = 'del'
    for ind, word in enumerate(MEname):
        print ind, word
        if word in dn.lower() :
            check.append(int(os.popen('grep -c pythia8'+ME[ind]+'Settings '+pi).read()))
            check.append(int(os.popen('grep -c "from Configuration.Generator.Pythia8'+ME[ind]+'Settings_cfi import *" '+pi).read()))
            check.append(int(os.popen('grep -c "pythia8'+ME[ind]+'SettingsBlock," '+pi).read()))
            if ind > 0 :
                 os.system('wget -q https://cms-pdmv.cern.ch/mcm/public/restapi/requests/get_fragment/'+pi+' -O '+my_path+'/'+pi+'/'+pi)
                 gridpack_cvmfs_path = os.popen('grep \/cvmfs '+my_path+'/'+pi+'/'+pi+'| grep -v \'#args\' ').read()
                 gridpack_cvmfs_path = gridpack_cvmfs_path.split('\'')[1]
                 os.system('tar xf '+gridpack_cvmfs_path+' -C'+my_path+'/'+pi)
                 fname = my_path+'/'+pi+'/'+'process/madevent/Cards/run_card.dat'
                 fname2 = my_path+'/'+pi+'/'+'process/Cards/run_card.dat'
                 if os.path.isfile(fname) is True :
                     ickkw = str(os.system('grep "= ickkw" '+fname))
                 elif os.path.isfile(fname2) is True :    
                     ickkw = str(os.system('grep "= ickkw" '+fname2))
                     print("icckw "+ickkw)
                 print("icckw "+ickkw)
                 matching = int(string.split(ickkw," ")[-1])
                 print(matching)
                 print
#            check.append(int(os.popen('grep -c pythia8'+ME[ind]+'Settings '+pi).read()))
#            check.append(int(os.popen('grep -c "from Configuration.Generator.Pythia8'+ME[ind]+'Settings_cfi import *" '+pi).read()))
#            check.append(int(os.popen('grep -c "pythia8'+ME[ind]+'SettingsBlock," '+pi).read()))
            if matching >= 2 and check[0] == 2 and check[1] == 1 and check[2] == 1 :
                print "no known inconsistency in the fragment w.r.t. the name of the dataset "+word
            elif matching < 2 and check[0] == 0 and check[1] == 0 and check[2] == 0 :    
                print "no known inconsistency in the fragment w.r.t. the name of the dataset "
            else:     
                print "Wrong fragment: "+word+" in dataset name but settings in fragment not correct or vice versa"
