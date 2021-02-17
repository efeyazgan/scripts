#!/usr/bin/env python

import sys
import os
import json


json1 = str(sys.argv[1])
json2 = str(sys.argv[2])
if len(sys.argv) != 3:
    print "Enter two json files to compare"
with open(json1) as j1:
    data1 = json.load(j1)
with open(json2) as j2:
    data2 = json.load(j2)
data1 = json.dumps(data1, sort_keys=True)
data2 = json.dumps(data2, sort_keys=True)
print "Json1:"
print data1
print "Json2:"
print data2
print "============================"
if data1 == data2:
    print "Two json files are identical"
else:
    print "Two json files are NOT identical"
