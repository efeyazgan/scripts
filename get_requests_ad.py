import os,sys,time
import string
import re
import argparse
import textwrap
os.system('source /afs/cern.ch/cms/PPD/PdmV/tools/McM/getCookie.sh')
os.system('cern-get-sso-cookie -u https://cms-pdmv.cern.ch/mcm/ -o ~/private/prod-cookie.txt --krb --reprocess')
sys.path.append('/afs/cern.ch/cms/PPD/PdmV/tools/McM/')

from rest import McM
from json import dumps
from itertools import groupby
from textwrap import dedent

mcm = McM(dev=False)
page = 0
nrequests = 0;
ntotalrequests = 0;
nevents = 0;
ntotalevents = 0;
#res = mcm.get('requests',query='prepid=MUO*&member_of_campaign=RunIIFall17wmLHEGS&status=defined', page=page)
res = mcm.get('requests',query='prepid=HIG*&member_of_campaign=RunIIFall18*GS', page=page)
while len(res) !=0:
        for r in res:
                if "jhugen" in r['dataset_name'].lower() and "submitted" in r['status'].lower():
                        print str(r['prepid'])+"  "+str(r['dataset_name'])+"  "+str(r['status'])
                ntotalrequests += 1
                ntotalevents += r['total_events']
#               if "nlo" not in r['dataset_name'].lower() and "fxfx" not in r['dataset_name'].lower() and "powheg" not in r['dataset_name'].lower() and "jhu" not in r['dataset_name'].lower():
#                      if "approved" in str(r['status']) or "defined" in str(r['status']): 
#                      if "done" in str(r['status']) and "tunecuet8m2t4" in r['dataset_name'].lower():  
#                               prepid_query = 'contains='+r['prepid']
#                               ticket = mcm.get('mccms',query=prepid_query)
#                               if ticket is not None: 
#                                       for tt in ticket:
#                                               if tt['block'] == 2 or tt['block'] == 1:
#                                                       print (str(r['prepid'])+"  "+str(r['dataset_name'])+"  "+str(r['total_events'])+"  "+str(r['status'])+"  "+str(tt['block']))
#                                                       nrequests += 1
#                                                       nevents += r['total_events']    
        page += 1
        res = mcm.get('requests',query='prepid=HIG*&member_of_campaign=RunIIFall18*GS', page=page)
        time.sleep(0.5)
#print "number of requests "+str(nrequests)
#print "total number of requests "+str(ntotalrequests)
#print float(nrequests)/float(ntotalrequests)
#print "  "
#print "number of events "+str(nevents)
#print "total number of events "+str(ntotalevents)
#print float(nevents)/float(ntotalevents)
