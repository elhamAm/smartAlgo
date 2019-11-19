from __future__ import division, print_function
from math import sqrt, log
from random import choice as rand_choice
from state import State
#import numpy as np
#import matplotlib.pyplot as plt

"""
Written by Y.Thorimbert

In this file we choose to represent a state of the problem as a list
of numbers in which number 16 denotes the empty cell.

Note that using State objects as implemented in state module, this
list for state x is stored as 'x.value'.

All the functions below are specific to "taquin" (or 15-Puzzle) game.
"""
nombreDeNoeudA = 0
nombreDeNoeud = 0

DIRECTIONS = ["up", "right", "down", "left"] #possible directions

def is_solution(x):
    """Check if the value of the state x is the list of numbers from 1 to 16.
    """
    return x.value == list(range(1, len(x.value) + 1))

def count_bad_cells(x):
    """Heuristic g(x) function: counts the number of misplaced cells."""
    count = 0
    for i, n in enumerate(x.value):
        if n != i + 1:
            count += 1
    return count

##def count_bad_cells(x): #equivalent
##    """Heuristic g(x) function: counts the number of misplaced cells."""
##    count = 0
##    for i in range(len(x.value)):
##        if x.value[i] != i + 1:
##            count += 1
##    return count

def gen_board_in_direction(board, direction):
    """This is a helper function for get_children.
    Returns the state of <board> after moving the empty cell in a given
    direction.
    """
    newboard = list(board) #copy original board
    l = len(board)
    n = int(sqrt(l))
    i = newboard.index(l) #index of empty cell
    j = i
    #moves the empty cell index according to the direction
    if direction == "up":
        j -= n
    elif direction == "down":
        j += n
    elif direction == "left":
        j -= 1
    elif direction == "right":
        j += 1
    newboard[i], newboard[j] = newboard[j], newboard[i] #swap elements
    return newboard

def get_children(x):
    """
    Returns a list of States instance containing all the possible children
    of x.
    """
    l = len(x.value)
    i = x.value.index(l)#index of element whose value is 'l' (=15)
    n = int(sqrt(l))
    possible_directions = list(DIRECTIONS)
    #remove impossible directions:
    if i % n == n - 1:
        possible_directions.remove("right")
    elif i % n == 0:
        possible_directions.remove("left")
    if i < n:
        possible_directions.remove("up")
    elif i > l - n - 1:
        possible_directions.remove("down")
    children = []
    #for each possible direction, append the corresponding children state:
    for direction in possible_directions:
        next_board = gen_board_in_direction(x.value, direction)
        sol = State(value = next_board, parent = x,depth = x.depth + 1, step = direction) #sol est de type state
        children.append(sol)
    return children

def gen_disorder(board, n):
    """
    Use this function to verify your algorithm. It produces a disordered board
    and the corresponding solution path as output.
    """
    x = State(board, None, 0, "start")
    solutions = [x]
    for i in range(n):
        children = get_children(x)
        choice = rand_choice(children) #pick a random child
        while choice.value in [sol.value for sol in solutions]:
            children.remove(choice)
            choice = rand_choice(children)
        solutions.append(choice)
        x = choice
    return solutions

def show_board(board, empty_symbol="O"):
    """This function simply displays a board. <board> is a list."""
    l = len(board)
    nformat = int(round(log(l, 10)) + 1) + 1 #+ 1 pour l'espace
    n = int(sqrt(l))
    line = 0
    column = 0
    i = 0
    while i < l:
        s = "{:>" + str(nformat) + "}"
        if board[i] == 16:
            number = empty_symbol
        else:
            number = str(board[i])
        print(s.format(number), end="")
        if i % n == n - 1:
            print("")
        i += 1
    print("")

def cost(node):
	#g(x) + h(x)
	return node.depth + count_bad_cells(node)


def costA(node):
	#g(x) + h(x)
	return node.depth
#insert the new child in live list
def addToLiveNodeList(child ,liveNodeList):

	liveNodeList.append( child )
	for i in range(len(liveNodeList)-1,0,-1): # loop backward

		c1 = cost(liveNodeList[i])
		c2 = cost(liveNodeList[i - 1])

		if c1 > c2:
			( liveNodeList [i] , liveNodeList [i - 1]) = (liveNodeList [i - 1] , liveNodeList [i] )
		else : break # because the other elements are sorted

	return liveNodeList

def addToLiveNodeListA(child ,liveNodeList):
	liveNodeList.append( child )
	for i in range(len(liveNodeList)-1,0,-1): # loop backward

		c1 = costA(liveNodeList[i])
		c2 = costA(liveNodeList[i - 1])

		if c1 > c2:
			( liveNodeList [i] , liveNodeList [i - 1]) = (liveNodeList [i - 1] , liveNodeList [i] )
		else : break # because the other elements are sorted

	return liveNodeList

def nextENode( liveNodeList ): 
	node = liveNodeList.pop() 
	return node
def P(node):
	if node.depth == cost(node): 
		return True
	return False

def inverse(step):
	if step == "up":
		step = "down"

	elif step == "down":
		step = "up"

	elif step == "left":
		step = "right"

	elif step == "right":
		step = "left"

	return step


def solve(board) :
	liveNodeList =[]
	E_node = board # root is the initial point
	path = []
	global nombreDeNoeud
	while not P(E_node):
		
		#print("here")
		nombreDeNoeud = nombreDeNoeud + 1
		#print("nombreDeNoeud",nombreDeNoeud)
		l = get_children(E_node)
		for child in l: 
			exists = 0
			for i in range(len(liveNodeList)):
				if liveNodeList[i].value == child.value:
					exists = 1
			if not exists:
				addToLiveNodeList(child ,liveNodeList)
		E_node = nextENode(liveNodeList)
		#print("chosen child premier while:", E_node.value, E_node.step)
		#path.append(E_node.step)
		#print("path: ",path)
	while (E_node.parent != None):
		#print("chosen child: deuxieme while", E_node.value, E_node.step)
		path.append((E_node.step))
		E_node = E_node.parent
	path.reverse()
	return path

def solvecaseA(board) :
	liveNodeList =[board]
	E_node = board # root is the initial point
	path = []
	global nombreDeNoeudA
	while count_bad_cells(E_node):#not P(E_node):
		E_node = nextENode(liveNodeList)
		#print("here")
		nombreDeNoeudA = nombreDeNoeudA + 1
		#print("nombreDeNoeud",nombreDeNoeud)
		l = get_children(E_node)
		for child in l: addToLiveNodeListA(child ,liveNodeList)
		
		#print("chosen child premier while:", E_node.value, E_node.step)
		#path.append(E_node.step)
		#print("path: ",path)
	while (E_node.parent != None):
		#print("chosen child: deuxieme while", E_node.value, E_node.step)
		path.append((E_node.step))
		E_node = E_node.parent
	path.reverse()
	return path









initial_board =  [1,   2,  3,  4,
                  5,   6, 16,  8,
                  9,  10,  7, 11,
                 13,  14, 15, 12]

initial_state = State(value=initial_board, parent=None, depth=0, step="start")
print("Initial state:")
show_board(initial_state.value)
print("Children:")
for child in get_children(initial_state):
	print("child", child.step)
	show_board(child.value)


path = solve(initial_state) 
print("path",path)
print("*****************************************************************")
initial_board = list(range(1, 4 * 4 + 1)) #solution ...
disorder_nodes = gen_disorder(initial_board, 10) # ... on met du desordre
#disorder_nodes contient maintenant une liste d'etats dont le dernier est le
#point de depart de la recherche (c'est l'etat le plus desordonne).
disordered_state = disorder_nodes[-1]
print("disordered state value", disordered_state.value);
initial_node = State(value = disordered_state.value, parent=None, depth = 0, step = "start")
#le path reponse
for i in range(len(disorder_nodes)-1,0,-1):
	print("va : ", inverse(disorder_nodes[i].step))
    #show_board(disorder_nodes[i].value)
path = solve(initial_node) 
print("path",path)
# print("*****************************************************************")

# nlist = []
# klist = []
# for n in range(1,12):
# 		nombreDeNoeud = 0
# 		print("n",n)
# 		nlist.append(n)

# 		for j in range(20):
			
# 			initial_board = list(range(1, 4 * 4 + 1)) 
# 			disorder_nodes = gen_disorder(initial_board, n) 
# 			disordered_state = disorder_nodes[-1]
# 			initial_node = State(value = disordered_state.value, parent=None, depth = 0, step = "start")
# 			solve(initial_node) 
# 		k = nombreDeNoeud / 20
# 		klist.append(k)
# 		print(k)
# plt.figure(2)
# plt.plot(nlist, klist)
# print(nlist)
# plt.xticks(np.arange(min(nlist), max(nlist) + 1, 1.0))

# plt.grid()
# plt.ylabel('k : le nombre de noeuds explorés')
# plt.xlabel('n : la distance du board jusqua la board ordonne en utilisant gen_disorder')
# plt.title("cout = g + h")
# plt.show()
# plt.close()

# nlistA = []
# klistA = []
# for n in range(1,7):
# 		nombreDeNoeudA = 0
# 		print("n",n)
# 		nlistA.append(n)

# 		for j in range(20):
			
# 			initial_board = list(range(1, 4 * 4 + 1)) 
# 			disorder_nodes = gen_disorder(initial_board, n) 
# 			disordered_state = disorder_nodes[-1]
# 			initial_node = State(value = disordered_state.value, parent=None, depth = 0, step = "start")
# 			solvecaseA(initial_node) 
# 		k = nombreDeNoeudA / 20
# 		klistA.append(k)
# 		print(k)
# plt.figure(1)
# plt.plot(nlistA, klistA)
# print(nlistA)
# plt.xticks(np.arange(min(nlistA), max(nlistA) + 1, 1.0))

# plt.grid()
# plt.ylabel('k : le nombre de noeuds explorés')
# plt.xlabel('n : la distance du board jusqua la board ordonne en utilisant gen_disorder')
# plt.title("cout = h")
# plt.show()
# plt.close()



