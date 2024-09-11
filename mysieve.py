from math import sqrt
def Liste_facteures(old_P,old_facteures,pold,pnext):
	facteures=old_facteures
	P=old_P*pold
	for f in range(pold,pnext):
		facteures.append(f)
	return facteures,P
def Liste_restes(old_restes,old_P,old_facteures,PBIS,x):
	pold=PBIS[x]
	if pold==3:pnext=5
	else:
		try:
			pnext=PBIS[x+1]
		except:pnext=7
	facteures,P=Liste_facteures(old_P,old_facteures,pold,pnext)
	restes=[1]
	for f in facteures:
		for r in old_restes:
			restes.append(P*f+r)
	x+=1
	PBIS+=old_restes[1:]
	return restes,P,facteures,PBIS,x
def filtrage(restes,PBIS,x):
	X=[]
	pold=PBIS[x]
	for xi in restes[1:]:
		if xi!=pold and xi%pold==0:
			continue
		X.append(xi)
	return [1]+X
PBIS=[2,3]
x=1
restes,P,facteures,PBIS,x=Liste_restes([1,5],2,[1,2],PBIS,x)
#print(filtrage(restes,PBIS,x))
#print([1,5],2,[1,2],PBIS,x)
#print(restes,PBIS)
number=3
for k in range(number):
	restes=filtrage(restes,PBIS,x)
	restes,P,facteures,PBIS,x=Liste_restes(restes,P,facteures,PBIS,x)
	#print(restes,PBIS)
divmax=int(sqrt(PBIS[-1]))+1
print(divmax)
Premiers=[]
xd=0
for xc in range(len(PBIS)):
	if PBIS[xc]>divmax:
		break
xd=xc-1
DIV=[11]+PBIS[x:xd]
for pbis in PBIS:
	for div in DIV:
		if pbis==div:
			Premiers.append(pbis)
			break
		elif pbis%div!=0:
			Premiers.append(pbis)
			break
print(Premiers,DIV)