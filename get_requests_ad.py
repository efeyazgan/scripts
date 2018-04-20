import os,sys,time
os.system('source /afs/cern.ch/cms/PPD/PdmV/tools/McM/getCookie.sh')
os.system('cern-get-sso-cookie -u https://cms-pdmv.cern.ch/mcm/ -o ~/private/prod-cookie.txt --krb --reprocess')
sys.path.append('/afs/cern.ch/cms/PPD/PdmV/tools/McM/')

from rest import *

mcm = restful(dev=False)

# example to search  ALL requesst which are member of a campaign
# it uses a generic search for specified columns: query='status=submitted'
# queries can be combined: query='status=submitted&member_of_campaign=Summer12'

#PhaseIISummer17wmLHEGENOnly, RunIISummer15wmLHEGS
page = 0
res = mcm.getA('requests',query='member_of_campaign=RunIIFall17wmLHEGS&dataset_name=*powheg*JHUGen*&status=submitted', page=page)
while len(res) != 0:
    for r in res:
        if "NLO" not in r['dataset_name']:
#            print ("'"+r['prepid']+"',")
            print ("'"+r['prepid']+"',",r['dataset_name'])# print(r['prepid']+',')
    page += 1
    res = mcm.getA('requests',query='member_of_campaign=RunIIFall17wmLHEGS&dataset_name=*powheg*JHUGen*&status=submitted', page=page)
    time.sleep(0.5)
