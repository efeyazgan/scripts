import os
import sys
import random
from contextlib import redirect_stdout
import subprocess, sys, shlex
main_path = '/tmp/efe/'
directory = r'/cvmfs/cms.cern.ch/phys_generator/gridpacks/UL/13TeV/madgraph/V5_2.6.5/g2HDM/ttc/'
for filename in os.listdir(directory):
    newdir = str(random.randint(500,1000))
    os.mkdir(newdir)
    os.chdir(newdir)
    process = subprocess.Popen('tar xf '+os.path.join(directory, filename),
            stdout=subprocess.PIPE,
            shell=True)
    (output, err) = process.communicate()
    process_status = process.wait()
    print("Output: ",output)
    print("Exist status: ",process_status)
    print("Error: ", err)
    process2 = subprocess.Popen('./runcmsgrid.sh 10 13434 1',
            stdout=subprocess.PIPE,
            shell=True)
    (output2, err2) = process2.communicate()
    process2_status = process2.wait()
    print("Output2: ",output2)
    print("Exit2 status: ",process2_status)
    print("Error2: ",err2)
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    os.chdir(main_path)
