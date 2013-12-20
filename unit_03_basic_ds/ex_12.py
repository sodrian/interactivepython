class Deque(object):
    def __init__(self):
        self.c = []

    def add_front(self, item):
        self.c.append(item)

    def add_rear(self, item):
        self.c.insert(0, item)

    def pop_front(self):
        try:
            return self.c.pop()
        except IndexError:
            raise IndexError('Deque is empty')

    def pop_rear(self):
        try:
            return self.c.pop(0)
        except IndexError:
            raise IndexError('Deque is empty')

    def is_empty(self):
        return len(self.c) == 0

    def size(self):
        return len(self.c)


class PolyndromChecked(object):
    def __init__(self, s):
        assert isinstance(s, str), 'Only strings are accepted'
        self.c = Deque()
        for sub_s in s:
            self.c.add_front(sub_s)

    def check(self):
        is_polyndrom = True
        while self.c.size() > 1 and is_polyndrom:
            is_polyndrom = self.c.pop_front() == self.c.pop_rear()
        return is_polyndrom
