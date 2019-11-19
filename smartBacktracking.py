from copy import deepcopy

def solveBackTrack(A, D, R2, R1, order):	
	#remove the unity restrictions from D
	#print("D: ", D)
	D = constrictR1(D, R1, order)
	print("D after unity constriction: ", D)
	AC3(order, D, R2)
	print("D after AC3: ", D)
	s = backTrack(A, D, R2, order)
	return s

def backTrack(A, D, R2, order):
	if(None not in A):
		return A

	for i in range(len(A)):
		if (not A[i]):
			ind = i
			break
	
	#print("ind: ", ind)
	#print("D: ", D)
	print("C = ", D[2], " P = ", D[1], "F = ", D[0])
	for ele in D[ind]:
		Atemp = deepcopy(A)
		Atemp[ind] = ele
		global step
		step=step + 1
		print("Etape", step,". AV ", "C = ", Atemp[2], " P = ", Atemp[1], "F = ", Atemp[0])
		#print(order[ind],": ", ele)
		#print("D: ", D)
		Dtemp = deepcopy(D)
		Dtemp = forwardCheck(Atemp, Dtemp, ind, R2, order)
		#print("Dtemp: ", Dtemp)
		if(Dtemp):
			return backTrack(Atemp, Dtemp, R2, order)

def AC3(order, D, R2):
	workList = []
	for x in order:
		for key in R2:
			if x in key:
				workList.append(key)
				
		while(True):
			couple = workList.pop()
			#see if couple actually works for all the values of one of the couples
			changed = reduce(x, order, D, couple)
			if(changed):
				if(not D):
					break
				else:
					for key in R2:
						if(x in key and (not key in workList)):
							workList.append(key)
			if(not workList):
				break
					
		

def reduce(x, order, D, couple):
	#(x,y) = couple
	if(x == couple[0]):
		y = couple[1]
	else:
		y = couple[0]
	#print("x: ", x, "y: ", y)	
	for i, ele in enumerate(order):
		#print("order: ", order)
		#print("ele: ", ele)
		if(ele == y):
			indy = i
		if(ele == x):
			indx = i
	#print("indy: ", indy)
	changed = False
	for xv in D[indx]:
		keepXV = False
		for yv in D[indy]:
			if((xv, yv) in R2.get(couple)):
				keepXV = True
		if(not keepXV):
			changed = True
			D[indx].remove(xv)
	return changed

	
def forwardCheck(A, D, ind, R2, order):
	#look at what I have to remove from the domain of others
	#my value is in A[ind]
	#make sure that A[ind],z exists
	#print("A: ", A)
	#print("ind: ", ind)
	xele = A[ind]
	for nex in range(ind, len(A)):
		let = order[ind]
		#print("x: ", let)
		nextLet = order[nex]
		#print("y: ", nextLet)
		#print((let, nextLet))
		for eleNext in D[nex]:
			#print("eleNext: ", eleNext)
			#print("xele: ", xele)
			if(R2.get(( let, nextLet))):
				if(not (xele, eleNext) in R2.get((let, nextLet))):
					D[nex].remove(eleNext)
					global step
					step= step+1
					print("Etape", step,". FC ", "C = ", D[2], " P = ", D[1], "F = ", D[0])

	return D
		
	
	
def constrictR1(D, R1, order):
	for i, cons in enumerate(R1):
		#print("const: ", cons)
		#print("i: ", i)
		for ele in D[i]:
			if not ele in R1.get(order[i]):
				global step
				step=step+1
				D[i].remove(ele)
				print("Etape", step, ". CU ", "C = ", D[2], " P = ", D[1], "F = ", D[0])
	return D
	
		
	


#main
#F P C
order = ["F", "P", "C"]
R2 = {
	("F","C") : [(1,4), (1,3), (2,4), (4,1), (3,1), (4,2)],
	("P", "C") : [(1,3), (1,4), (2,3), (2,4), (3,1), (4,1), (3,2), (4,2)],
	("F","C") : [(1,4), (1,3), (2,4), (4,1), (3,1), (4,2)],
	("P", "C") : [(1,3), (1,4), (2,3), (2,4), (3,1), (4,1), (3,2), (4,2)]
	
}

R1 = {
	"F": [2,3],
	"P": [2,3]
}
step = 0
s = solveBackTrack([None, None, None], [[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]], R2, R1, order)
print("solution: ", s)
