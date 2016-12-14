class QueueRear(object):
    def __init__(self):
        self.c = []

    def enqueue(self, item):
        self.c.insert(0, item)

    def dequeue(self):
        self.c.pop()

    def is_empty(self):
        return self.size() == 0

    def size(self):
        return len(self.c)
