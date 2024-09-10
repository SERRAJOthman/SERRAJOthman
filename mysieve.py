premiers=[2]
sortie=premiers
facteurs=[1,2]
P=2
restes=[1]
for init in range(3):
	#Calcul des facteurs
	F=premiers[-1]
	for o in range(facteurs[-1]+1,F):
		facteurs.append(o)
	#Calcul des h futur r
	H=[]
	for f in facteurs:
		for r in restes:
			H.append(P*f+r)
	r1=H[0]
	P*=r1
	restes=[1]+H
	sortie+=H
	print("sortie:",sortie)