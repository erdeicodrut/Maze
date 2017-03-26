from Queue import *
from Node import *
from Maze import *

numOfNodes = 5

Q = Queue()
field = Maze(numOfNodes)
nodes = [Node() for x in range(numOfNodes + 1)]

field.add(0, 1, 0)
field.add(1, 2, 2)
field.add(1, 3, 3)
field.add(2, 4, 4)
field.add(3, 5, 1)
field.add(4, 5, 1)

startNode = 0
nodes[startNode].visited = True


def showPath(endNode):
    i = endNode
    while nodes[i].prev is not None:
        print(nodes[i])
        i = nodes[i].prev.num

def search_djikstra(this_node_num):
    pos = 0

    for node in field.adjacence[this_node_num]:

        if node != 100 and nodes[pos].visited == False:
            nodes[pos].visited = True
            nodes[pos].prev = nodes[this_node_num]
            nodes[pos].value = nodes[this_node_num].value + node
            Q.push(nodes[pos])
            Q.sort()

        pos += 1

        if this_node_num == numOfNodes:
            print("Node found w/ value {}".format(nodes[this_node_num].value))
            break
    curr = Q.pop()
    if curr is None:
        return
    curr = curr.num
    search_djikstra(curr)


search_djikstra(startNode)

showPath(numOfNodes)