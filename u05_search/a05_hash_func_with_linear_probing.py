#!/usr/bin/env python


class HashTable(object):
    def __init__(self, table_size):
        assert isinstance(table_size, int)
        assert 0 < table_size < 100
        self.t_s = table_size
        self.c = [None for i in range(table_size)]

    def try_to_find_free_slot(self, slot):
        found = False
        iters = 0
        while not found and iters <= len(self.c):
            slot += 1
            iters += 1
            if self.c[slot] is None:
                found = True
        return slot

    def add(self, item):
        assert isinstance(item, int)
        slot = item % self.t_s
        if self.c[slot] is None:
            self.c[slot] = item
        else:
            slot = self.try_to_find_free_slot(slot)
            if slot:
                self.c[slot] = item

    def print_table(self):
        s = '-' * (self.t_s * 4 + 1) + '\n'
        for el in self.c:
            s += '|{0:3}'.format(el or '')
        s += '|\n'
        s += '-' * (self.t_s * 4 + 1)
        print(s)


if __name__ == '__main__':
    t = HashTable(11)
    t.add(113)
    t.add(117)
    t.add(97)
    t.add(100)
    t.add(114)
    t.add(108)
    t.add(116)
    t.add(105)
    t.add(99)
    t.print_table()