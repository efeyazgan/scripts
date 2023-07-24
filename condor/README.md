```cond_sub_gripack_generation.py``` is used to produce gridpacks to be run under ```genproductions/bin/MadGraph5_aMCatNLO``` .



```cond_sub.py``` calculates cross-section after matching with PYTHIA8 starting from a template mcm request. 
To be run in ```CMSSW_12_4_8``` in el8. 
In condor:
```
python3 cond_sub.py
```
Or locally, e.g.:
```
python3 condor_get_cross_section_from_prepid_to_cmsrun_gridpack.py --file g2HDM_ttc_s0_M350_rhotu08_rhotc00_rhott00_slc7_amd64_gcc700_CMSSW_10_6_0_tarball.tar.xz --interference 0 #or 1
```
Once all are done, a cross-section table is created by running:
```
python read_cross_sections.py
```
