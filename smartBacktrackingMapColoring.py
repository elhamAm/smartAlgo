from copy import deepcopy

#la 4ième partie
def choisirCouleur(couleurs, D, ind):
	#print("ind: ", ind)
	#print("D[ind]: ", D[ind])
	if(D[ind]):
		#print("here")
		#c= D[ind].pop()
		colRes = None
		smallestCont = 100000
		for col in D[ind]:
			cont = 0
			for vos in voisins[ind]:
				if not col in D[vos]:
					cont = cont + 1
			
			if smallestCont > cont:
				colRes = col
				smallestCont = cont
		D[ind].remove(colRes)
		return colRes
	return -1
	
#la première partie
def sansHeuristic(couleurs):
	for i in range(len(couleurs)):
		if(not couleurs[i]):
			ind = i
			return i

#la deuxième partie
def plusContrainteHeuristic(couleurs):
	reg = None
	biggestSize = -10
	for i in range(len(couleurs)):
		colorOfNeigh =[]
		if(not couleurs[i]):
			for vos in voisins[i]:
				if(couleurs[vos] and (not couleurs[vos] in colorOfNeigh)):
					colorOfNeigh.append(couleurs[vos])
			if(biggestSize < len(colorOfNeigh)):
				biggestSize = len(colorOfNeigh)
				reg = i
	return reg
#la troisième partie
def plusContraignanteHeuristic(couleurs):		
	reg = None
	biggestSize = -10
	for i in range(len(couleurs)):
		noColor=0;
		if(not couleurs[i]):
			for vos in voisins[i]:
				if(not couleurs[vos]):
					noColor = noColor+1
			if(biggestSize < noColor):
				biggestSize = noColor
				reg = i
	return reg
		
def valid(couleurs, ind, voisins):
	for vos in voisins[ind]:
		#print("number of the voisin: ", vos)
		#print("color od the voisin: ", couleurs[vos])
		if(couleurs[ind] == couleurs[vos]):
			return False
	return True
		
	
def backTracking(level, couleurs, D, voisins, func):
	#AC3()
	if(level == 0):
		ind = 0
	else:	
		#choisir le noeud à traiter
		if(not None in couleurs):
			return couleurs
		ind = func(couleurs)
	print("cette region va etre developpée: ", ind)
	#choisir la couleur pour la region ind
	#print("DIIIICTTT: ",dictEnvers)
	#print(dictEnvers.get(ind))
	while(True):
		c = choisirCouleur(couleurs, D, ind)
		if(c == -1):
			return None
		couleurs[ind] = c
		#print("couleurs: ", couleurs)
		if valid(couleurs, ind, voisins):
			newLevel = level+1
			newD = deepcopy(D)
			newCouleurs = deepcopy(couleurs)
			print("cette combinaison de couleur: ", couleurs, " était valide et on va aller plus loin")
			res = backTracking(newLevel, newCouleurs, newD, voisins, func)
			if res:
				return res
		else:
			print("cette combinaison de couleur: ", couleurs, " n'était pas valide")
			
	return None
	


	
def createDomain(n, dicLen):
	D = []
	for j in range(dicLen):
		d = []
		for i in range(n):
			d.append(i+1)
		D.append(d)
			
		
	return D		
		


def createVoisins():
	voisins = []
	for reg in dict:
		v = []
		for t in R2:
			if (reg in t):
				voisInd = t.index(reg)
				voisInd = (voisInd-1) % 2
				vois = t[voisInd]
				v.append(dict.get(vois))
				#v.append(vois)
		voisins.append(v)
	return voisins
		
		

def printColorOfRegions(couleurs):
	for i, col in enumerate(couleurs):
		print(dictEnvers.get(i), " : ", col)

		

#main
n = 10


dict= { 
	'NB':0,
	'CA':1,
	'V':2,
	'MPLR':3,
	'RAA':4,
	'PACA':5,
	'PLCB':6
	}


dictEnvers= { 
	0:'NB',
	1:'CA',
	2:'V',
	3:'MPLR',
	4:'RAA',
	5:'PACA',
	6:'PLCB'
	}

R2 = [('V', 'NB'), ('V', 'PLCB'), ('NB', 'PLCB'), ('V', 'RAA'), ('PLCB', 'CA'), ('PLCB', 'RAA'), ('CA', 'RAA'), ('CA', 'MPLR'), ('MPLR', 'RAA'), ('RAA', 'PACA'), ('MPLR', 'PACA')]

#  **********************************************************************         première partie   ******************************************************************************
print("***************************** première partie **********************************")
for i in range(n):
	print("-----------------------------------------------------------------------------------------------")
	print("essayons avec ", i, " couleurs")
	D = createDomain(i, len(dict))
	voisins = createVoisins()
	#print("D: ", D)
	#print("voisins: ", voisins)
	couleurs = [None for i in range(len(dict))]
	couleursRes = backTracking(0, couleurs, D, voisins, sansHeuristic)
	if(couleursRes):
		print("************************** the minimal number of the colors is: ", i)
		printColorOfRegions(couleursRes);
		break
#  **********************************************************************         deuxième partie   ******************************************************************************
	
print("***************************** deuxième partie **********************************")
for i in range(n):
	print("-----------------------------------------------------------------------------------------------")
	print("essayons avec ", i, " couleurs")
	D = createDomain(i, len(dict))
	voisins = createVoisins()
	#print("D: ", D)
	#print("voisins: ", voisins)
	couleurs = [None for i in range(len(dict))]
	couleursRes = backTracking(0, couleurs, D, voisins, plusContrainteHeuristic)
	#print("couleurs: ", couleurs)
	if(couleursRes):
		print("***************************** the minimal number of the colors is: ", i)
		printColorOfRegions(couleursRes);
		break


#  **********************************************************************         troisième  partie   ******************************************************************************


print("***************************** troisième partie **********************************")
for i in range(n):
	print("-----------------------------------------------------------------------------------------------")
	print("essayons avec ", i, " couleurs")
	D = createDomain(i, len(dict))
	voisins = createVoisins()
	print("D: ", D)
	#print("voisins: ", voisins)
	couleurs = [None for i in range(len(dict))]
	couleursRes = backTracking(0, couleurs, D, voisins, plusContraignanteHeuristic)
	#print("couleurs: ", couleurs)
	if(couleursRes):
		print("****************************** the minimal number of the colors is: ", i)
		printColorOfRegions(couleursRes);
		break


