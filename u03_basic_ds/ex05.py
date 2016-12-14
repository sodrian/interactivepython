#!/usr/bin/env python


class QueueRear(object):
    def __init__(self):
        self.c = []

    def __str__(self):
        return str(self.c)

    def enq(self, item):
        self.c.insert(0, item)

    def deq(self):
        self.c.pop()

    @property
    def is_empty(self):
        return self.size == 0

    @property
    def size(self):
        return len(self.c)


if __name__ == '__main__':
    q = QueueRear()
    q.enq(34)
    q.enq(43)
    q.enq(23)
    q.enq(65)
    print(q)
    print(q.size)