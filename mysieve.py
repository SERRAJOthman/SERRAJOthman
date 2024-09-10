premiers=[2,3,5,7]
sortie=premiers
facteurs=[1,2]
P=2
restes=[1]
for init in range(3):
	F=sortie[init+1]
	G=sortie[init+2]
	for o in range(facteurs[-1]+1,F):
		facteurs.append(o)
	H=[]
	for f in facteurs:
		for r in restes:
			H.append(P*f+r)
	if init<1:P*=H[0]
	else:P*=restes[2]
	X=[]
	for x in H[2:]:
		if x%F==0 or x%G==0:
			continue
		X.append(x)
	restes=[1]+H[:2]+X
	sortie+=X
	print("sortie:",sortie)