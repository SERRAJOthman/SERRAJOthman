premiers=[2]
sortie=premiers
facteurs=[1,2]
P=2
restes=[1]
for init in range(3):
	F=premiers[-1]
	for o in range(facteurs[-1]+1,F):
		facteurs.append(o)
	H=[]
	for f in facteurs:
		for r in restes:
			H.append(P*f+r)
	P*=H[0]
	restes=[1]+H
	sortie+=H
	print("sortie:",sortie)