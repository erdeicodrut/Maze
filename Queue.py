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
        self.que.append(who)
        self.end = len(self.que)

    def __str__(self):
        print([q for q in self.que])

    # def sort(self):
    #     for i in range(self.start, self.end - 1):
    #         for j in range(i, self.end):
    #             if self.que[i] > self.que[j]:
    #                 swap(self.que[i], self.que[j])

    def sort(self):
        for passnum in range(len(self.que) - 1, self.start, -1):
            for i in range(passnum):
                if self.que[i] > self.que[i + 1]:
                    temp = self.que[i]
                    self.que[i] = self.que[i + 1]
                    self.que[i + 1] = temp



def swap(a, b):
    aux = a
    a = b
    b = aux

