class Stack(object):
    def __init__(self):
        self.c = []

    def push(self, item):
        self.c.append(item)

    def pop(self):
        return self.c.pop()

    def is_empty(self):
        return len(self.c) == 0


def divide_by_2(num):
    assert isinstance(num, (int)), 'Num must be int'
    s = Stack()

    while num:
        rem = num % 2
        s.push(rem)
        num //= 2

    r = ''
    while not s.is_empty():
        r += str(s.pop())

    if not r:
        r = '0'

    return r
