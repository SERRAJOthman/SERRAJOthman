premiers=[2,3,5,7]
sortie=premiers
facteurs=[1,2]
P=2
restes=[1]
c=1
for init in range(4):
	F=sortie[init+1]
	c+=1
	for o in range(facteurs[-1]+1,F):
		facteurs.append(o)
	H=[]
	for f in facteurs:
		for r in restes:
			H.append(P*f+r)
	if init<1:P*=H[0]
	else:P*=restes[2]
	X=[]
	u=0
	for x in H[2:]:
		for ci in range(1,c):
			if x%sortie[init+ci]==0:
				u=0
				break
			else:u=1
		if u==1:X.append(x)
	restes=[1]+H[:2]+X
	sortie+=X
	print("sortie:",sortie)