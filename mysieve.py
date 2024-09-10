def Liste_facteures(old_P,old_facteures,pold,pnext):
	facteures=old_facteures
	P=old_P*pold
	for f in range(pold,pnext):
		facteures.append(f)
	return facteures,P
def Liste_restes(old_restes,old_P,pold,pnext,old_facteures):
	facteures,P=Liste_facteures(old_P,old_facteures,pold,pnext)
	restes=[1]
	for f in facteures:
		for r in old_restes:
			restes.append(P*f+r)
	return restes,P,pnext,restes[1],facteures
def sievage(Hilk,x):
	g=Hilk[x]
	Hulk=Hilk[:x+1]
	for m in Hilk[x:]:
		if m%g!=0:
			Hulk.append(m)
	return Hulk,g
old_restes,old_P,pold,pnext,old_facteures=Liste_restes([1,5],2,3,5,[1,2])
print([1,5],2,3,5,[1,2])
Hilk=[2,3,5]
print(Hilk)
x=1
for k in range(2):
	x+=1
	Hilk+=old_restes[1:]
	print(Hilk,sievage(Hilk,x))
	print(old_restes,old_P,pold,pnext,old_facteures)
	old_restes,old_P,pold,pnext,old_facteures=Liste_restes(old_restes,old_P,pold,pnext,old_facteures)
print(old_restes,old_P,pold,pnext,old_facteures)
x+=1
Hilk+=old_restes[1:]
print(Hilk,sievage(Hilk,x))