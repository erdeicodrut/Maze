class Maze:
    def __init__(self, nodes):
        self.adjacence = [[100 for x in range(nodes + 1)] for y in range(nodes + 1)]

    def get(self, i, j):
        if i < 40 and j < 40:
            return self.adjacence[i][j]

    def add (self, i, j, val = 1):
        self.adjacence[i][j] = val
        self.adjacence[j][i] = val
