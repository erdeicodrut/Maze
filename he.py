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
# Q.push(nodes[startNode])


def walk_through(this_node_num):
    pos = 0

    # print([da for da in Q.que])

    for node in field.adjacence[this_node_num]:

        if node != 100 and nodes[pos].visited == False:
            nodes[pos].visited = True
            nodes[pos].prev = nodes[this_node_num]
            nodes[pos].value = nodes[this_node_num].value + node
            Q.push(nodes[pos])
            # print([da.num > Q.start for da in Q.que])
            # print([da.num for da in Q.que])
            Q.sort()
            # print([da.num > Q.start for da in Q.que])
            # print([da.num for da in Q.que])

        pos += 1

        if this_node_num == numOfNodes:
            print("Node found w/ value {}".format(nodes[this_node_num].value))
            break

    curr = Q.pop().num
    print(curr)
    walk_through(curr)

walk_through(startNode)

for i in field.adjacence:
    for j in i:
        print(j, end=" ")
    print()

print([x.num for x in Q.que])