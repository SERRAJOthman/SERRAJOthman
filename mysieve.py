#premiers=[2]
#facteurs=[1]
#restes=[1,5]
#1<reste(n)<produit_premiers(n)-1
#1<facteur(n)<premier(n+1)-1
#formule_produit_premier=
#produit_premiers(i)*facteur(j)+reste(k)
def Lrestes(premiers):
	P=1
	restes=[]
	for premier in premiers:
		P*=premier
	for o in range(1,P):
		restes.append(o)
		for premier in premiers:
			if restes[-1]%premier==0: 
				restes.pop()
	return restes,P
def Lfacteurs(premiers):
	F=premiers[-1]
	facteurs=[]
	for t in range(1,F+1):
		facteurs.append(t)
	return facteurs
#restes,P=Lrestes(premiers)
#facteurs=Lfacteurs(premiers)
#H=P,facteurs,restes
#print(H)
def formule_produit_premier(H):
	premiers_potentiels=[]
	for f in facteurs:
		for r in restes:
			h=P*f+r
			premiers_potentiels.append(h)
	return premiers_potentiels
#premiers_bis=premiers+restes[1:]+formule_produit_premier(H)
#print(premiers_bis)

def formule_generale(n):
	premiers=[2,3]
	premiers_potentiels=[7,11,13,17,19,23]
	for l in range(n):
		P=1
		facteurs=[]
		restes=[]
		for premier in premiers:
			P*=premier
		for o in range(1,P):
			restes.append(o)
			for premier in premiers:
				if restes[-1]%premier==0: 
					restes.pop()
		F=premiers[-1]
		for t in range(1,F+1):
			facteurs.append(t)
	premiers_potentiels=[]
	for f in facteurs:
		for r in restes:
			h=P*f+r
			premiers_potentiels.append(h)
	premiers_bis=premiers+restes[1:]+premiers_potentiels
	premiers.append(restes[1])
	return premiers,restes,facteurs,premiers_potentiels	
print(formule_generale(2))
