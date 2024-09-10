premiers=[2,3,5]
sortie=premiers
facteurs=[1,2]
P=6
restes=[1,5]
print("restes:",restes)
for init in range(2):
	print("premiers:",premiers)
	#Calcul des facteurs
	F=premiers[-1]
	for o in range(facteurs[-1]+1,F):
		facteurs.append(o)
	print("facteurs:",facteurs)
	#Calcul des h futur r
	H=[]
	for f in facteurs:
		for r in restes:
			print(P,f,r)
			H.append(P*f+r)
	h0=H[0]
	P*=restes[1]
	premiers.append(h0)
	print("P:",P)
	print("H:",H)
	print("premiers:",premiers)
	X=[]
	for x in H:
		if x%premiers[-2]!=0 or x==premiers[-2]:
			X.append(x)
	restes=[1]+X
	print("restes:",restes)
	sortie+=restes[1:]
	print("sortie:",sortie)