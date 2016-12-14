from random import randint


class Queue(object):
    def __init__(self, cont=None):
        if not cont:
            cont = []

        assert isinstance(cont, (list, tuple, set)), \
            "Only list, tuple or set is accepted as an argument"

        self.cont = list(cont)

    def __len__(self):
        return len(self.cont)

    def add(self, item):
        self.cont.append(item)

    def remove(self):
        try:
            item = self.cont.pop(0)
        except IndexError:
            raise IndexError('Queue is empty')
        return item

    def size(self):
        return len(self)

    def is_empty(self):
        return self.size() == 0


class PriorityQueue(object):
    def __init__(self, priorities):
        assert isinstance(priorities, (tuple, list, set)), 'Only tuple, list, set is accepted'

        self.cont = {}
        for pr in priorities:
            self.cont[pr] = []

    def add(self, item, priority):
        assert priority in self.cont, 'no queue with this name'
        self.cont[priority].append(item)

    def remove(self, priority):
        assert priority in self.cont, 'no queue with this name'
        try:
            return self.cont[priority].pop(0)
        except IndexError:
            raise IndexError('the queue is empty')


class HotPotatoSimulator(object):
    def __init__(self, cont):
        assert isinstance(cont, (list, tuple, set)), \
            'Only list, tuple and set is accepted as argument'
        assert 2 <= len(cont) <= 7, 'Iterable must be in range [2,7]'
        self.q = Queue(cont)

    def play(self):
        while not self.q.is_empty():
            cycles = randint(10, 20)
            for _ in range(cycles):
                item = self.q.remove()
                self.q.add(item)
            item = self.q.remove()
            print('{0} is gone...'.format(item))


class PrintTask(object):
    def __init__(self, time):
        self.enter_time = time
        self.exit_time = None


class PrintQueue(Queue):
    pass


class PrinterClassSimulation(object):
    PAGE_RATE = 60

    def __init__(self, students):
        assert isinstance(students, int), 'only int is accepted'
        assert students in range(1, 21), 'student amount must be in range [1, 20]'

        self.students = students
        self.queue = PrintQueue()
        self.processed_tasks = []

    def start(self):
        for m in range(60):
            curr_time = m
            for __ in range(self.students):
                if randint(0, 100) <= 20:
                    for ___ in range(randint(1, 20)):
                        t = PrintTask(curr_time)
                        self.queue.add(t)

            for __ in range(self.PAGE_RATE):
                try:
                    t = self.queue.remove()
                except IndexError:
                    continue
                t.exit_time = curr_time
                diff = t.exit_time - t.enter_time
                self.processed_tasks.append(diff)

            print(sum(self.processed_tasks) / len(self.processed_tasks))
