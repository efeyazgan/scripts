#############################
# git clone https://github.com/AndreasAlbert/lhereader.git
# pip install lhereader
# pip install scikit-hep
# python setup.py install
#############################

import numpy as np
from lhereader import LHEReader
from matplotlib import pyplot as plt 
#from histbook import *
#import vegascope; canvas = vegascope.LocalCanvas()
from operator import add 
import skhep
from skhep.math import LorentzVector

#reader = LHEReader('events/unweighted_events_cgbhp.lhe')
reader = LHEReader('events/unweighted_events_tHpm.lhe')

# Mediator mass in each event
mhiggs = []
mhiggs_plus = []
mhiggs_minus = []
mhiggs_cut = []
mtop = []
mtop_cut = []
pt_lep = []
eta_lep = []
pt_lep_cut = []
eta_lep_cut = []
pt_b = []
eta_b = []
pt_b_cut = []
eta_b_cut = []
pt_b_de_higgs = []
eta_b_de_higgs = []
pt_b_de_top = []
eta_b_de_top = []
pt_nu = []
pt_nu_cut = []
b_parent = []
num_b = []
counter = 0
particle_add = np.array([0,0,0,0])
for iev, event in enumerate(reader):
    # Find H+
    higgs = filter(lambda x: abs(x.pdgid) == 5000003, event.particles)
    cut = 0
    accept_lep = 0
    accept_b = 0
    accept_nu = 0
    n_b = 0
    b_from_higgs = []
    higgs_index = []
    higgs_ind = 0
    top_ind = []
#    if iev > 4:
#        continue
    test = 0
#    print(iev, "size=",len(event.particles))
    for ind, y in enumerate(event.particles):
#        print(iev,ind,y)
        if abs(y.pdgid) == 5 and y.status != -1:
            n_b += 1
#        if iev == 2140:
#        if ind == 2 or ind == 3:
#        print(ind,y)
        if abs(y.pdgid) == 6:
            top_ind.append(ind + 1)
        if abs(y.pdgid) == 5000003:
            higgs_ind = ind + 1
            higgs_index.append(higgs_ind)
#            if ind != 2:
#                print(iev,ind,y)
#                test = 1
#        if test == 1:
#            print("Two jet event?:")
#            print(iev,ind,y)
        if y.parent == higgs_ind and higgs_ind:
            particle_add = np.vstack((particle_add,y.p4()))
        if abs(y.pdgid) == 5 and y.parent == higgs_ind and higgs_ind:
            b_from_higgs.append(ind)
        if (abs(y.pdgid) == 11 or abs(y.pdgid) == 13) and (y.p4().pt > 30 and abs(y.p4().eta) < 2.5) and y.status == 1:
            accept_lep += 1
        if abs(y.pdgid) == 5 and y.p4().pt > 20 and abs(y.p4().eta) < 2.4 and y.status == 1:
            accept_b += 1
        if  (abs(y.pdgid) == 12 or abs(y.pdgid) == 14) and y.p4().pt > 35 and y.status == 1:
            accept_nu += 1    
    num_b.append(n_b)   
#    print(iev,b_from_higgs)
#    if n_b > 2:
#        print(iev)        
#    final_sum = np.sum(particle_add,axis=0)
#    final_sum = LorentzVector(final_sum[0],final_sum[1],final_sum[2],final_sum[3])
    # Sum over all higgs four-momenta in the event
    combined_p4 = None
    for p4 in map(lambda x: x.p4(), higgs):
        if combined_p4:
            combined_p4 += p4
        else:
            combined_p4 = p4
    if combined_p4:
        mhiggs.append(combined_p4.mass)
        if accept_lep == 1 and accept_b >= 2 and accept_nu == 1:
            mhiggs_cut.append(combined_p4.mass)
################
    higgs_plus = filter(lambda x: x.pdgid == 5000003, event.particles) 
    combined_p4p = None
    for p4 in map(lambda x: x.p4(), higgs_plus):
        if combined_p4p:
            combined_p4p += p4
        else:
            combined_p4p = p4 
#        print(iev,"plus",combined_p4p,combined_p4p.mass)    
    if combined_p4p:
        mhiggs_plus.append(combined_p4p.mass)
        
    higgs_minus = filter(lambda x: x.pdgid == -5000003, event.particles) 
    combined_p4m = None
    for p4 in map(lambda x: x.p4(), higgs_minus):
        if combined_p4m:
            combined_p4m += p4
        else:
            combined_p4m = p4 
#        print(iev,"plus",combined_p4p,combined_p4p.mass)    
    if combined_p4m:
        mhiggs_minus.append(combined_p4m.mass)        
        
    top = filter(lambda x: abs(x.pdgid) == 6, event.particles)
    combined_top_p4 = None
    for p4 in map(lambda x: x.p4(), top):
        if combined_top_p4:
            combined_top_p4 += p4
        else:
            combined_top_p4 = p4
    if combined_top_p4:
        mtop.append(combined_top_p4.mass)
        if accept_lep == 1 and accept_b >= 2 and accept_nu == 1:
            mtop_cut.append(combined_top_p4.mass)
        
    lep = filter(lambda x: abs(x.pdgid) == 11 or abs(x.pdgid) == 13, event.particles)
    combined_lep_p4 = None
    for p4 in map(lambda x: x.p4(), lep):
        if combined_lep_p4:
            combined_lep_p4 += p4
        else:
            combined_lep_p4 = p4
    if combined_lep_p4:
        pt_lep.append(combined_lep_p4.pt)   
        eta_lep.append(combined_lep_p4.eta) 
        if accept_lep == 1 and accept_b >= 2 and accept_nu == 1:
            pt_lep_cut.append(combined_lep_p4.pt)   
            eta_lep_cut.append(combined_lep_p4.eta)
        
    bquark = filter(lambda x: abs(x.pdgid) == 5  and x.status == 1, event.particles)
    bquark_prime = filter(lambda x: abs(x.pdgid) == 5  and x.status == 1, event.particles)
    bquark_accepted = filter(lambda x: abs(x.pdgid) == 5  and x.status == 1 and x.p4().pt > 20 and abs(x.p4().eta) < 2.4, event.particles)
    combined_b_p4 = None
    for p4 in map(lambda x: x.p4(), bquark):
        pt_b.append(p4.pt)   
        eta_b.append(p4.eta)   

    for what in map(lambda x:x.parent, bquark_prime):
        b_parent.append(what)
 
    bquark_de_higgs = filter(lambda x: abs(x.pdgid) == 5  and x.status == 1 and x.p4().pt > 20 and abs(x.p4().eta) < 2.4 and x.parent == higgs_ind, event.particles)
    for p4 in map(lambda x: x.p4(), bquark_de_higgs):
        pt_b_de_higgs.append(p4.pt) 
        eta_b_de_higgs.append(p4.eta)     
        
#    print(iev,top_ind)    
    bquark_de_top = filter(lambda x: abs(x.pdgid) == 5  and x.status == 1 and x.p4().pt > 20 and abs(x.p4().eta) < 2.4 and x.parent in top_ind, event.particles)
    for p4 in map(lambda x: x.p4(), bquark_de_top):
        pt_b_de_top.append(p4.pt) 
        eta_b_de_top.append(p4.eta)              
        
#    for ind, y in enumerate(event.particles):
#        print(iev,ind,y)


    combined_b_acc_p4 = None
    for p4 in map(lambda x: x.p4(), bquark_accepted):
        pt_b_cut.append(p4.pt)   
        eta_b_cut.append(p4.eta)    
    
    nu = filter(lambda x: abs(x.pdgid) == 12 or abs(x.pdgid) == 14, event.particles)
    combined_nu_p4 = None
    for p4 in map(lambda x: x.p4(), nu):
        if combined_nu_p4:
            combined_nu_p4 += p4
        else:
            combined_nu_p4 = p4
    if combined_nu_p4:
        pt_nu.append(combined_nu_p4.pt) 
        if accept_lep == 1 and accept_b >= 2 and accept_nu == 1:
            pt_nu_cut.append(combined_nu_p4.pt) 
              
################

print(f'Mean charged higgs mass: {np.mean(mhiggs)}')
print(f'Median charged higgs mass: {np.median(mhiggs)}')
print(f'Mean charged higgs mass after cuts: {np.mean(mhiggs_cut)}')
print(f'Median charged higgs mass after cuts: {np.median(mhiggs_cut)}')
print(f'Mean top mass: {np.mean(mtop)}')
print(f'Median top mass: {np.median(mtop)}')

plt.figure(1)
plt.hist(mhiggs,density=False,label="Higgs$\pm$",histtype="step",bins=200,range=(200,400))
#plt.hist(mhiggs_plus,density=False,label="Higgs+",histtype="step",bins=200,range=(200,400))
#plt.hist(mhiggs_minus,density=False,label="Higgs-",histtype="step",bins=200,range=(200,400))
plt.hist(mhiggs_cut,density=False,label="Higgs with cuts",histtype="step",bins=200,range=(200,400))
plt.xlabel('m(H$^\pm$) [GeV]')
plt.yscale('log')
plt.legend(loc='upper right')
textstr = "Mean mass\n"+\
        "H+/-="+str(round(np.mean(mhiggs),1))+"GeV\n"+\
        "H+  ="+str(round(np.mean(mhiggs_plus),1))+"GeV\n"+\
        "H-  ="+str(round(np.mean(mhiggs_minus),1))+"GeV\n\n"+\
        "Median mass\n"+\
        "H+/-="+str(round(np.median(mhiggs),1))+"GeV\n"+\
        "H+  ="+str(round(np.median(mhiggs_plus),1))+"GeV\n"+\
        "H-  ="+str(round(np.median(mhiggs_minus),1))+"GeV"
plt.text(200, 10, textstr)
plt.savefig('charged_higgs_mass.png')

plt.figure(2)
plt.hist(mtop,density=False,label="Top",histtype="step",bins=200,range=(140,200))
plt.hist(mtop_cut,density=False,label="Top w/ cuts",histtype="step",bins=200,range=(140,200))
plt.xlabel('m(top) [GeV]')
plt.legend(loc='upper right')
plt.savefig('top_mass.png')

plt.figure(3)
plt.hist(pt_lep,density=False,label="Leptons",histtype="step",bins=200,range=(0,200))
plt.hist(pt_lep_cut,density=False,label="Leptons w/ cuts",histtype="step",bins=200,range=(0,200))
plt.xlabel('pT(lepton) [GeV]')
plt.legend(loc='upper right')
plt.savefig('pt_lepton.png')

plt.figure(4)
plt.hist(eta_lep,density=False,label="Leptons",histtype="step",bins=200,range=(-5.2,5.2))
plt.hist(eta_lep_cut,density=False,label="Leptons w/ cuts",histtype="step",bins=200,range=(-5.2,5.2))
plt.xlabel('$\eta$(lepton) [GeV]')
plt.legend(loc='upper right')
plt.savefig('eta_lepton.png')

plt.figure(5)
plt.hist(pt_b,density=False,label="b quark",histtype="step",bins=200,range=(0,200))
plt.hist(pt_b_cut,density=False,label="b quark w/ cuts",histtype="step",bins=200,range=(0,200))
plt.hist(pt_b_de_higgs,density=False,label="b quark w/ cuts - parent H+/-",histtype="step",bins=200,range=(0,200))
plt.hist(pt_b_de_top,density=False,label="b quark w/ cuts - parent Top",histtype="step",bins=200,range=(0,200))
plt.xlabel('pT(b quark) [GeV]')
plt.legend(loc='upper right')
plt.savefig('pt_b.png')

plt.figure(6)
plt.hist(eta_b,density=False,label="b quark",histtype="step",bins=200,range=(-5.2,5.2))
plt.hist(eta_b_cut,density=False,label="b quark w/ cuts",histtype="step",bins=200,range=(-5.2,5.2))
plt.hist(eta_b_de_higgs,density=False,label="b quark w/ cuts - parent H+/-",histtype="step",bins=200,range=(-5.2,5.2))
plt.hist(eta_b_de_top,density=False,label="b quark w/ cuts - parent Top",histtype="step",bins=200,range=(-5.2,5.2))
plt.xlabel('$\eta$(b quark) [GeV]')
plt.legend(loc='upper right')
plt.savefig('eta_b.png')

plt.figure(7)
plt.hist(pt_nu,density=False,label="MET",histtype="step",bins=200,range=(0,200))
plt.hist(pt_nu_cut,density=False,label="MET w/ cuts",histtype="step",bins=200,range=(0,200))
plt.xlabel('pT(\u03BD) [GeV]')
plt.legend(loc='upper right')
plt.savefig('pt_nu.png')


plt.figure(8)
plt.hist(b_parent,density=False,label="b parents",histtype="step",bins=10,range=(0.5,10.5))
plt.xlabel('parent ID')
plt.legend(loc='upper right')
plt.savefig('b_parent.png')

plt.figure(9)
plt.hist(num_b,density=False,label="number of final state b quarks",histtype="step",bins=10,range=(0.5,10.5))
plt.xlabel('n(b)')
plt.legend(loc='upper right')
plt.savefig('number_of_final_state_b_quarks.png')

plt.show()

