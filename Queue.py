class Queue:
    def __init__(self):
        self.que = []
        self.start = 0
        self.end = 0

    def pop(self):
        if self.end - self.start > 0:
            self.start += 1
            return self.que[self.start - 1]

    def push(self, who):
        self.end += 1
        self.que.append(who)

    def sort(self):
        for i in range(self.start, self.end + 1):
            for j in range(self.start, self.end + 1):
                if self.que[i] > self.que[j]:
                    swap(self.que[i], self.que[j])


def swap(a, b):
    aux = a
    a = b
    b = aux

