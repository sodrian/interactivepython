#!/usr/bin/env python
import random
from datetime import datetime, timedelta


class QueueAbstract(object):
    def __init__(self):
        self.c = []

    @property
    def is_empty(self):
        return len(self.c) == 0


class Queue(QueueAbstract):
    def enqueue(self, item):
        self.c.append(item)

    def dequeue(self):
        try:
            return self.c.pop(0)
        except IndexError:
            raise IndexError('The queue is empty')


class QueueRear(QueueAbstract):
    def enqueue(self, item):
        self.c.insert(0, item)

    def dequeue(self):
        try:
            return self.c.pop()
        except IndexError:
            raise IndexError('The queue is empty')


def random_els():
    for _ in xrange(random.randint(0, 100000)):
        yield random.randint(0, 100000)
    return


def timedelta_to_seconds(t_d):
    assert isinstance(t_d, timedelta), 'not a timedelta object'
    s = float(t_d.seconds) + float(t_d.microseconds) / 1000000
    return s


def benchmark():
    random_lst = list(random_els())

    q1 = Queue()
    q2 = QueueRear()
    first_timing = 0.0
    second_timing = 0.0

    t1 = datetime.now()
    for el in random_lst:
        q1.enqueue(el)
    t2 = datetime.now()
    first_timing += timedelta_to_seconds(t2 - t1)

    t1 = datetime.now()
    for el in random_lst:
        q2.enqueue(el)
    t2 = datetime.now()
    second_timing += timedelta_to_seconds(t2 - t1)

    t1 = datetime.now()
    while not q1.is_empty:
        q1.dequeue()
    t2 = datetime.now()
    first_timing += timedelta_to_seconds(t2 - t1)

    t1 = datetime.now()
    while not q2.is_empty:
        q2.dequeue()
    t2 = datetime.now()
    second_timing += timedelta_to_seconds(t2 - t1)

    print(first_timing, second_timing, second_timing/first_timing)


if __name__ == '__main__':
    benchmark()
