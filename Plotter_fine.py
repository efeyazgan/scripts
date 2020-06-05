import ROOT
import sys
import os

def plot_mc_data(outname,list1,list2):
	pname=outname
	pList=list1
	pList2=list2

	ROOT.gStyle.SetOptStat(0)
	ROOT.gStyle.SetOptTitle(0)
	c=ROOT.TCanvas('c','c',500,500)

	histos=[]
	for p,title,color in pList:
		histos.append( f1.Get(p) )
		if "inc_nbjets" in histos[-1].GetName():
			c.SetLogy()
		histos[-1].SetLineWidth(2)
		histos[-1].SetLineColor(color)
		histos[-1].SetTitle(title)
		histos[-1].DrawNormalized('Esame' if len(histos)>1 else 'E')
	for p,title,color in pList2:
		histos.append( f2.Get(p) )
		histos[-1].SetLineWidth(2)
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
print(hist_list[1])

for x in hist_list:
	pname = x
	pList=[(x,'ttbar dilepton',1)]
	pList2=[(x,'ttc-MA0-200-rtc04',2)]
	plot_mc_data(pname,pList,pList2)



#all done
f1.Close()
f2.Close()
