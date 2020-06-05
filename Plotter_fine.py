import ROOT
import sys
import os
from ROOT import TCanvas, TFile, TProfile, TNtuple, TH1F, TH2F
from ROOT import gROOT, gBenchmark, gRandom, gSystem
import ctypes

def plot_mc_data(outname,list1,list2):
	pname=outname
	pList=list1
	pList2=list2

	ROOT.gStyle.SetOptStat(0)
	ROOT.gStyle.SetOptTitle(0)
	c=ROOT.TCanvas('c','c',500,500)

	histos=[]
	for p,title,color in pList:
		print(p,title,color)
		histos.append( f1.Get(p) )
		histos[-1].SetLineColor(color)
		histos[-1].SetTitle(title)
		histos[-1].DrawNormalized('Esame' if len(histos)>1 else 'E')
	for p,title,color in pList2:
		histos.append( f2.Get(p) )
		histos[-1].SetLineColor(color)
		histos[-1].SetTitle(title)
		histos[-1].DrawNormalized('hist same' if len(histos)>1 else 'hist')


	c.BuildLegend(0.65,0.95,0.95,0.8)
	c.Modified()
	c.Update()
	c.SaveAs(pname+'.pdf')


#open root file
f1=ROOT.TFile.Open(sys.argv[1])
f2=ROOT.TFile.Open(sys.argv[2])


hist_list = os.popen('rootls -1 '+sys.argv[1]).read().split('\n')
hist_list = list(filter(None, hist_list))
print("first file contents:")
print(hist_list)
hist_list2 = os.popen('rootls -1 '+sys.argv[2]).read().split('\n')
hist_list2 = list(filter(None, hist_list2))
print("second file contents:")
print(hist_list2)

for x in hist_list:
	pname = x
	pList=[(x,'ttbar dilepton',1)]
	pList2=[(x,'ttc-MA0-200-rtc04',2)]
	plot_mc_data(pname,pList,pList2)



#all done
f1.Close()
f2.Close()
