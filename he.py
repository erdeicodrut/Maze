from Queue import *
from Node import * 
from Maze import *

numOfNodes = 5

Q = Queue()
field = Maze(numOfNodes)
nodes = [ Node() for x in range(numOfNodes + 1)]


field.add(0,1,0)
field.add(1,2,2)
field.add(1,3,3)    
field.add(2,4,4)
field.add(3,5,1)
field.add(4,5,1)

startNode = 0
Q.push(nodes[startNode])




def walkthrough(thisNodesNum):
	for node, pos in field.adjacence[thisNodesNum], range(6):
		
		if (thisNodesNum == 5):
			print("Node found w/ value {}".format(nodes[thisNodesNum].value))

		if (node != None and nodes[pos].visited == False):
			nodes[pos].visited = True
			nodes[pos].prev = nodes[thisNodesNum]
			nodes[pos].value = nodes[thisNodesNum].value + node
			Q.push(nodes[pos])
			Q.pop()
			Q.sort()
			walkthrough(Q.pop().num)
			


walkthrough(startNode)



	


