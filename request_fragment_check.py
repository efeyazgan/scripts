import os,sys,time
os.system('source /afs/cern.ch/cms/PPD/PdmV/tools/McM/getCookie.sh')
os.system('cern-get-sso-cookie -u https://cms-pdmv.cern.ch/mcm/ -o ~/private/prod-cookie.txt --krb --reprocess')
sys.path.append('/afs/cern.ch/cms/PPD/PdmV/tools/McM/')

from rest import McM
from json import dumps

mcm = McM(dev=True)

res = mcm.get('requests', query='prepid=TOP-RunIISummer15wmLHEGS-00023')

for r in res:
    pi = r['prepid']
    dn = r['dataset_name']
    print ("'"+r['prepid']+"',",r['dataset_name'])
    os.system('wget -q https://cms-pdmv.cern.ch/mcm/public/restapi/requests/get_fragment/'+pi+' -O '+pi)
    if "powheg" in dn or "Powheg" in dn or "POWHEG" in dn :
        powheg_check = os.popen('grep -c pythia8PowhegEmissionVetoSettings '+pi).read()
        print "no known inconsistency in the fragment w.r.t. the name of the dataset"
        powheg_check = int(powheg_check)
        if powheg_check == 0 :
            print "Wrong fragment: powheg in dataset name but no pythia8PowhegEmissionVetoSettings in fragment"
