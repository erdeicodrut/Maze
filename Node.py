anum = 0

class Node:

    def __init__(self):
        self.visited = False
        self.prev = None
        self.value = 0
        
        global anum
        self.num = anum
        anum = self.num + 1

    def __gt__(self, other):
        if self.value < other.value:
            return True
        else:
            return False

    def __str__(self):
        return self.num
