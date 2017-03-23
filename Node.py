anum = 0

class Node:

    def __init__(self):
        global anum
        self.visited = False
        self.prev = None
        self.value = 0
        self.num = anum
        anum = self.num

    def __gt__(self, other):
        if self.value > other.value:
            return True
        else:
            return False