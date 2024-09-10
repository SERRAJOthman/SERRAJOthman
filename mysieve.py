premiers=[2,3,5,7]
sortie=premiers
number=2
for init in range(number):
	print("premiers:",premiers)
	#Calcul des facteurs
	n=len(premiers)-2
	F=premiers[n+1]
	facteurs=[]
	for o in range(1,F):
		facteurs.append(o)
	print("facteurs:",facteurs)
	#Calcul des restes
	restes=[]
	P=1
	for p in premiers[:n+1]:P*=p#mettre au debut
	for t in range(1,P):
		restes.append(t)
		for premier in premiers:
			if restes[-1]%premier==0:
				restes.pop()
	print("restes:",restes)
	sortie+=restes[1:]
	print("sortie:",sortie)
	#Calcul des h
	H=[]
	for f in facteurs:
		for r in restes:
			H.append(P*f+r)
	premiers.append(restes[1])
	print("H:",H,"premiers:",premiers)