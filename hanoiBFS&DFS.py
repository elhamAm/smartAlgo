from copy import deepcopy

class Node2():
	def __init__(self, p1, p2, p3):
		self.p1 = p1
		self.p2 = p2
		self.p3 = p3
		self.pre = None
	def __eq__(self, other):
		return (self.p1 == other.p1 and self.p2 == other.p2 and self.p3 == other.p3)
	def isGoal(self):
		return (self.p1 == [] and self.p2 == [])
def mini(p):
	if(p == []):
		return 1000000
	else: 	
		return min(p) 
def nextNodes2(current):

	stackOfNext = []
	if(current.p1 and mini(current.p1) < mini(current.p2)):
		nextN = deepcopy(current)
		nextN.pre = current
		nextN.p2.append(mini(current.p1))
		nextN.p1.remove(mini(current.p1))
		stackOfNext.append(nextN)
		
	if(current.p2 and mini(current.p2) < mini(current.p3)):
		nextN = deepcopy(current)
		nextN.pre = current
		nextN.p3.append(mini(current.p2))
		nextN.p2.remove(mini(current.p2))
		stackOfNext.append(nextN)

	if(current.p3 and mini(current.p3) < mini(current.p1)):
		nextN = deepcopy(current)
		nextN.pre = current
		nextN.p1.append(mini(current.p3))
		nextN.p3.remove(mini(current.p3))
		stackOfNext.append(nextN)
		
	if(current.p2 and mini(current.p2) < mini(current.p1)):
		nextN = deepcopy(current)
		nextN.pre = current
		nextN.p1.append(mini(current.p2))
		nextN.p2.remove(mini(current.p2))
		stackOfNext.append(nextN)
		
	if(current.p3 and mini(current.p3) < mini(current.p2)):
		nextN = deepcopy(current)
		nextN.pre = current
		nextN.p2.append(mini(current.p3))
		nextN.p3.remove(mini(current.p3))
		stackOfNext.append(nextN)
		
	if(current.p1 and mini(current.p1) < mini(current.p3)):
		nextN = deepcopy(current)
		nextN.pre = current
		nextN.p3.append(mini(current.p1))
		nextN.p1.remove(mini(current.p1))
		stackOfNext.append(nextN)
	return stackOfNext

def printQueue(queue):
	for v in queue:
		printOne(v)

def printOne(v):
	print("____")
	print("p1: ", v.p1, "p2: ", v.p2, "p3: ", v.p3)
	print("____")
def bfs(start, successors):
	visited = []

	notVisited = []
	notVisited.append(start)

	
	while(notVisited):
		#print("not visited: ", len(n))
		#print("*****relecture*****")
		#for no in visited:
		#	print("-------------")
		#	print("m: ", no.m)
		#	print("c: ", no.c)
		#	print("b: ", no.b)

		#print("visited: ", len(visited))
		current = notVisited.pop()

		print("not visited: ")
		printQueue(notVisited)
		print("current: ")
		printOne(current)


		visited.append(current)

		if(current.isGoal()):
			print("etat trouve!!")
			return current
		nexts = successors(current)

		for succ in nexts:
			if succ in visited:
				continue
			if succ not in notVisited:
				notVisited.append(succ)


		
		#print("visited: ", len(visited))

def dfs(start, successors):
	visited = []

	notVisited = []
	notVisited.append(start)

	
	while(notVisited):
		#print("not visited: ", len(n))
		#print("*****relecture*****")
		#for no in visited:
		#	print("-------------")
		#	print("m: ", no.m)
		#	print("c: ", no.c)
		#	print("b: ", no.b)

		#print("visited: ", len(visited))
		current = notVisited.pop()

		print("not visited: ")
		printQueue(notVisited)
		print("current: ")
		printOne(current)

		
		visited.append(current)

		if(current.isGoal()):
			print("etat trouve!!")
			return current
		nexts = successors(current)

		for succ in nexts:
			if succ in visited:
				continue
			if succ not in notVisited:
				notVisited.insert(0, succ)


		
		#print("visited: ", len(visited))
def makePath(current):
	path = []
	while(current.pre):
		path.append(current)
		current = current.pre
	path.append(current)
	return path[::-1]
		

	
	

##main

#question1.1
print("---------------premiere question bfs-------------")
n=3
start = Node2([i for i in range(0,n)][::-1],[],[])
goal = bfs(start, nextNodes2)
path = makePath(goal)
for node in path:
	print("poteau1: ",node.p1," poteau2: ",node.p2, "poteau3: ", node.p3)


print("---------------premiere question dfs-------------")
n=3
start = Node2([i for i in range(0,n)][::-1],[],[])
goal = dfs(start, nextNodes2)
path = makePath(goal)
for node in path:
	print("poteau1: ",node.p1," poteau2: ",node.p2, "poteau3: ", node.p3)
