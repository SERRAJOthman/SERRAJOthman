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
number=4
for k in range(number):
	restes=filtrage(restes,PBIS,x)
	restes,P,facteures,PBIS,x=Liste_restes(restes,P,facteures,PBIS,x)
Premiers=PBIS
divmax=int(sqrt(PBIS[-1]))
for xc in range(x,len(PBIS)):
	Premiers=filtrage(Premiers,PBIS,xc)
	if PBIS[xc]>divmax:break
Premiers=[2]+Premiers[1:]
print(Premiers)