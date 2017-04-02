import cv2
import numpy as np
from Node import *
from Queue import *
from Maze import *
# from he import search_djikstra

nodes = []
field = Maze(len(nodes))
Q = Queue()


def distance(xa, ya, xb, yb):
    return np.sqrt((xa - xb) ** 2 + (ya - yb) ** 2)


def showPath(endNode):
    i = endNode
    while nodes[i].prev is not None:
        if nodes[i].x < len(maze) and nodes[i].y: maze[nodes[i].x][nodes[i].y] = 127
        i = nodes[i].prev.num
    if nodes[i].x < len(maze) and nodes[i].y: maze[nodes[i].x][nodes[i].y] = 127


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

        if this_node_num == len:
            print("Node found w/ value {}".format(nodes[this_node_num].value))
            break
    curr = Q.pop()
    if curr is None:
        return
    curr = curr.num
    search_djikstra(curr)


# checking if a node was found before
def found_before(node):
    for n in nodes:
        if n.x == node.x and n.y == node.y:
            return True
    return False


def get_node(x, y):
    for n in nodes:
        if n.x == x and n.y == y:
            return n
    return None

maze = []

def decode(path):
    global nodes
    # reading the image in grayscale
    global maze
    maze = cv2.imread(path, 0)

    # iterating through the pixels
    for j in range(1, len(maze) - 1):
        for i in range(1, len(maze[j]) - 1):

            
            # creating a temporary node
                temp = Node()
                temp.x = j                    
                temp.y = i

                # if the node wasn't found before add it into the set of nodes
                if found_before(temp) is False:
                    nodes.append(temp)
                    maze[i][j] = 200

    # creating the adjacence matrix
    field = Maze(len(nodes))

    for node in nodes:
        i = 0
        j = 0
        while True:

            i += 1

            if maze[node.x + i][node.y] == 255:
                if get_node(node.x + i, node.y) and found_before(get_node(node.x, node.y)):

                    get_node(node.x + i, node.y).prev = get_node(node.x, node.y)

                    field.add(node.num,
                              get_node(node.x + i, node.y).num,
                              distance(node.x, node.y, get_node(node.x + i, node.y).x, get_node(node.x + i, node.y).y))


            if node.x + i >= len(maze) - 1:
                break
            if maze[node.x + i][node.y] == 0:
                break

        while True:

            j += 1

            if maze[node.x][node.y + j] != 0:
                if get_node(node.x, node.y + j):

                    get_node(node.x, node.y + j).prev = get_node(node.x, node.y)

                    field.add(node.num, get_node(node.x, node.y + j).num, distance(node.x, node.y, get_node(node.x, node.y + j).x, get_node(node.x, node.y + j).y))


            if node.y + j >= len(maze) - 1:
                break
            if maze[node.x][node.y + j] == 0:
                break





# new shit {

def decodeAtor(path):
    global nodes
    # reading the image in grayscale
    global maze
    maze = cv2.imread(path, 0)

    # iterating through the pixels
    for j in range(1, len(maze) - 1):
        for i in range(1, len(maze[j]) - 1):

            # checking every pixel
            if maze[i][j] != 0:
                temp = Node()
                temp.x = j
                temp.y = i

            # if the node wasn't found before add it into the set of nodes
                if found_before(temp) is False:
                    nodes.append(temp)
                    maze[i][j] = 200

    # creating the adjacence matrix
    field = Maze(len(nodes))

    for node in nodes:
        i = 0
        j = 0
        while True:

            i += 1

            if maze[node.x + i][node.y] == 255:
                if get_node(node.x + i, node.y) and found_before(get_node(node.x, node.y)):

                    get_node(node.x + i, node.y).prev = get_node(node.x, node.y)

                    field.add(node.num,
                              get_node(node.x + i, node.y).num,
                              distance(node.x, node.y, get_node(node.x + i, node.y).x, get_node(node.x + i, node.y).y))


            if node.x + i >= len(maze) - 1:
                break
            if maze[node.x + i][node.y] == 0:
                break

        while True:

            j += 1

            if maze[node.x][node.y + j] != 0:
                if get_node(node.x, node.y + j):

                    get_node(node.x, node.y + j).prev = get_node(node.x, node.y)

                    field.add(node.num,
                              get_node(node.x, node.y + j).num, 
                              distance(node.x, node.y, get_node(node.x, node.y + j).x, get_node(node.x, node.y + j).y))

            if node.y + j >= len(maze) - 1:
                break
            if maze[node.x][node.y + j] == 0:
                break



# new shit }

decodeAtor("maze.png")

search_djikstra(0)  

showPath(nodes[len(nodes) - 2].num)

cv2.imwrite("imgu.png", maze)