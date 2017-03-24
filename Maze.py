class Maze:
    def __init__(self, nodes):
        self.adjacence = [[None for x in range(nodes + 1)] for y in range(nodes + 1)]

    def get(self, i, j):
        return self.adjacence[i][j]

    def add (self, i, j, val):
        self.adjacence[i][j] = val
        self.adjacence[j][i] = val
