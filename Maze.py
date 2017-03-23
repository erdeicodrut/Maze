class Maze:
    def __init__(self, nodes):
        self.adjacence = [[0 for x in range(nodes)] for y in range(nodes)]

    def get(self, i, j):
        return self.adjacence[i][j]

    def add (self, val, i, j):
        self.adjacence[i][j] = val
        self.adjacence[j][i] = val

