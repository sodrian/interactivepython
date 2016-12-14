class Deque(object):
    def __init__(self, cont=None):
        if cont is None:
            cont = []
        assert isinstance(cont, (list, tuple, set)), 'only list, tuple and set is accepted'
        self.cont = list(cont)

    def __len__(self):
        return len(self.cont)

    def add_front(self, item):
        self.cont.append(item)

    def add_rear(self, item):
        self.cont.insert(0, item)

    def pop_front(self):
        try:
            return self.cont.pop()
        except IndexError:
            raise IndexError('Deque is empty')

    def pop_rear(self):
        try:
            return self.cont.pop(0)
        except:
            raise IndexError('Deque is empty')

    def size(self):
        return len(self)

    def is_empty(self):
        return self.cont == []


class PolyndromChecher(object):
    def __init__(self, s):
        assert isinstance(s, str), 'only string is accepted'
        self.deque = Deque([ch for ch in s])

    def check(self):
        is_polyndrom = True
        while self.deque.size() > 1 and is_polyndrom:
            is_polyndrom = self.deque.pop_front() == self.deque.pop_rear()
        return is_polyndrom
