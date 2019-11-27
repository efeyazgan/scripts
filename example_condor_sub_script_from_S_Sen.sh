#! /bin/bash
SDIR="/afs/cern.ch/work/s/ssen/Professor/CMSSW_10_1_4/src/CP5-mc-CONDOR/6"
WDIR="/tmp/ssen/work"
ODIR="/afs/cern.ch/work/s/ssen/Professor/CMSSW_10_1_4/src/CP5-mc-CONDOR/6/out"
OTAG="OUT"
j=0
while [ $j -lt 4 ]
do
  let "j=j+1"
  echo $j
cat > subscript_$j.sh <<EOF 
#!/bin/bash
pushd ${CMSSW_BASE}/src/
export SCRAM_ARCH=slc6_amd64_gcc630
export RIVET_DATA_PATH=/afs/cern.ch/work/s/ssen/Professor/CMSSW_10_1_4/src/GeneratorInterface/RivetInterface/data
export RIVET_REF_PATH=/afs/cern.ch/work/s/ssen/Professor/CMSSW_10_1_4/src/GeneratorInterface/RivetInterface/data
echo \${PWD}
eval \`scram runtime -sh\`
#source Rivet/rivetSetup.sh
scram arch
popd
echo \${PWD}
mkdir -p ${WDIR}_$j
cd ${WDIR}_$j
cp ${SDIR}/CP5_20.py .
echo \${PWD}
ls -lrt 
which cmsRun
cmsRun CP5_20.py 
cp *yoda ${ODIR}/$j.yoda
cd ${ODIR}
echo \${PWD}
#rm -r -f ${WDIR}_$j
EOF
cat > condor_$j.sub <<EOF 
universe              = vanilla
executable            = subscript_$j.sh
output                = hello_$j.out
error                 = hello_$j.err
log                   = hello_${cluster}_${process}.log
+JobFlavour           = "espresso"
queue
EOF
  chmod 755 subscript_$j.sh
  chmod 755 condor_$j.sub
  condor_submit condor_$j.sub
done
