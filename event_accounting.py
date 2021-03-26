import os,sys,time
import string
import re
import argparse
import textwrap
from operator import itemgetter

os.system('env -i KRB5CCNAME="$KRB5CCNAME" cern-get-sso-cookie -u https://cms-pdmv.cern.ch/mcm/ -o cookiefile.txt --krb --reprocess')
#os.system('source /afs/cern.ch/cms/PPD/PdmV/tools/McM/getCookie.sh')
#os.system('cern-get-sso-cookie -u https://cms-pdmv.cern.ch/mcm/ -o ~/private/prod-cookie.txt --krb --reprocess')
sys.path.append('/afs/cern.ch/cms/PPD/PdmV/tools/McM/')

from rest import McM
from json import dumps
from itertools import groupby
from textwrap import dedent
import pandas as pd

#mcm = McM(cookie='cookiefile.txt', dev=False, debug=False)
mcm = McM(id='no-id', dev=False, debug=False)
mcm_link = "https://cms-pdmv.cern.ch/mcm/"

def get_request(prepid):
    result = mcm._McM__get('public/restapi/requests/get/%s' % (prepid))
    if not result:
        return {}

    result = result.get('results', {})
    return result

tot_kevt = 0
tot_cpu_ksec = 0
#f = open("Jan2021_application_assessment.txt",'r')
f = open("Revised20Jan2021genstudyDavid.txt",'r')
Lines = f.readlines()
for line in Lines:
    if line.startswith("#") is False:
        split_strings = line.split()    
        pid = line.split('|')[1].strip()
        res = get_request(pid)
        res = [res]
        for r in res:
            if "SUS-RunIISummer20UL18wmLHEGEN-00044" in pid or "EXO-RunIISummer20UL18wmLHEGEN-00130" in pid or "SUS-RunIISummer20UL18GEN-00013" in pid or "SUS-RunIISummer20UL18wmLHEGEN-00018" in pid or "EXO-RunIISummer20UL18GEN-00075" in pid:
                split_strings.insert(19,"?????????? | ???????") 
#            elif "SUS-RunIISummer20UL18wmLHEGEN-00044" not in pid and "EXO-RunIISummer20UL18wmLHEGEN-00130" not in pid and "SUS-RunIISummer20UL18GEN-00013" not in pid: 
            else:
#                print(pid)
                split_strings.insert(19,r['dataset_name'])
                final_string = ' '.join(split_strings)
                print " | "+split_strings[1].center(36)+" | "+split_strings[3].rjust(8)+" | "+split_strings[5].rjust(7)+" | "+split_strings[7].rjust(6)+" | "+split_strings[9].rjust(8)+" | "+split_strings[11].rjust(5)+" | "+split_strings[13].rjust(8)+" | "+split_strings[15].rjust(12)+" | "+str((21)*float(split_strings[15])/float(split_strings[3])).rjust(12)+" | "+split_strings[19].ljust(95)
#                if ("amcatnlo" not in r['dataset_name'].lower() and "fxfx" not in r['dataset_name'].lower() and "powheg" not in r['dataset_name'].lower()) and ("ww" in r['dataset_name'].lower() or "wz" in r['dataset_name'].lower() or "zz" in r['dataset_name'].lower()) and "hto" not in r['dataset_name'].lower() and "GluGluTo" not in r['dataset_name'] and "higgs" not in r['dataset_name'].lower() and "TWZ" not in r['dataset_name']: 
                #if "DYToHppHmm" not in r['dataset_name'] and (r['dataset_name'].lower().startswith("dy") or r['dataset_name'].lower().startswith("wjets") or  "usJets" in r['dataset_name'] or (r['dataset_name'].lower().startswith("w") and "Jets" in r['dataset_name'])) and ("mlm" in r['dataset_name'].lower()):
#                if r['dataset_name'].lower().startswith("qcd"):
#                if r['dataset_name'].lower().startswith("gjets"):
#                if r['dataset_name'].startswith("ST_") and "comphep" not in r['dataset_name']:
                if "mlm" in r['dataset_name'].lower() and (r['dataset_name'].lower().startswith("ttz") or r['dataset_name'].lower().startswith("ttw")):
                #if "HT500Njet" not in r['dataset_name'] and "openloops" not in r['dataset_name'].lower() and (r['dataset_name'].lower().startswith("ttto") or r['dataset_name'].lower().startswith("ttbb") or r['dataset_name'].lower().startswith("ttjets")):
#                if "b_bbar_4l" in r['dataset_name'].lower():
#                if "EXO" not in pid and "SUS" not in pid and "B2G" not in pid and "scalar" not in r['dataset_name'].lower() and "dm" not in r['dataset_name'].lower() and "fcnc" not in r['dataset_name'].lower() and "chargedhiggs" not in r['dataset_name'].lower() and "anom" not in r['dataset_name'].lower() and "BBA" not in r['dataset_name'] and "hplus" not in r['dataset_name'].lower():
#                    tot_kevt += float(split_strings[3])
#                    tot_cpu_ksec += float(split_strings[15])    
#                    print(final_string)
#                if r['dataset_name'].lower().startswith("wjet") and "HT" in r['dataset_name']:

#                    print r['dataset_name'].ljust(95)+" | "+str(float(split_strings[3])*1000./1E6).rjust(8)+" | "+str(float(split_strings[15])*1000./1.E9).rjust(12)+" | "+str(float(split_strings[15])/float(split_strings[3])).rjust(12)+" | "+str((21)*float(split_strings[15])/float(split_strings[3])).rjust(12)
                tot_kevt += float(split_strings[3])
                tot_cpu_ksec += float(split_strings[15])
#                print(final_string)
print "tot evt [M] | tot_cpu_sec [B s] | cpu per event [s] | HS06 per event [s]"

#print str(tot_kevt*1000./1E6)+" | "+str(tot_cpu_ksec*1000./1.E9)+" | "+str(tot_cpu_ksec/tot_kevt)+" | "+str((190./5.33)*tot_cpu_ksec/tot_kevt)

print str(tot_kevt*1000./1E6)+" | "+str(tot_cpu_ksec*1000./1.E9)+" | "+str(tot_cpu_ksec/tot_kevt)+" | "+str((21)*tot_cpu_ksec/tot_kevt)

#while len(res) !=0:
#    for r in res:
#        print str(r['prepid'])+"  "+str(r['dataset_name'])+"  "+str(r['status']+"   "+str(r['completed_events']))  
#        ntotalrequests += 1
#        ntotalevents += r['total_events']
#        ntotalcompletevents += r['completed_events']
#    page += 1
##    res = mcm.get('requests',query='member_of_campaign=RunIISummer19UL16wmLHEGEN&status=done', page=page)
