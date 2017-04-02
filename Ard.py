from Maze import *
from Node import *
from Queue import *
import time
import serial

ser = serial.Serial('/dev/ttyACM0', 9600)



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

def b(num):
    return bytes(num)

def showPath(endNode):
    i = endNode
    print("path:", end=" ")
    ser.write(str(endNode).encode('utf-8'))
    while nodes[i].prev is not None:
        print(nodes[i], end=", ")
        i = nodes[i].prev.num
        ser.write(str(i).encode('utf-8'))
        time.sleep(1)
    print(nodes[i])


def search_dijkstra(this_node_num):
    pos = 0

    for node in field.adjacence[this_node_num]:

        if node != 100 and nodes[pos].visited == False:
            nodes[pos].visited = True
            nodes[pos].prev = nodes[this_node_num]
            nodes[pos].value = nodes[this_node_num].value + node
            Q.push(nodes[pos])
            Q.sort()
            time.sleep(1)
            ser.write(str(nodes[pos].num).encode('utf-8'))

        pos += 1

        if this_node_num == numOfNodes:
            print("Node found w/ value {}".format(nodes[this_node_num].value))
            break
    curr = Q.pop()
    if curr is None:
        return
    curr = curr.num
    search_dijkstra(curr)


search_dijkstra(startNode)

ser.write(str(9).encode('utf-8'))
ser.write(str(9).encode('utf-8'))
time.sleep(1)

showPath(numOfNodes)