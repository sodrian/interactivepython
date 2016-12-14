#!/usr/bin/env python


class HashTable(object):
    def __init__(self):
        self.size = 11
        self.keys = [None] * self.size
        self.values = [None] * self.size

    def calc_hash(self, key):
        return key % self.size

    def rehash(self, old_hash):
        return (old_hash + 1) % self.size

    def put(self, key, value):
        hash_value = self.calc_hash(key)

        # the slot is empty and can be filled
        if self.keys[hash_value] is None:
            self.keys[hash_value] = key
            self.values[hash_value] = value

        # the slot is taken by the given key
        # new value must be entered
        elif self.keys[hash_value] == key:
            self.values[hash_value] = value

        # first empty slot must be used
        # if failed to find empty slots, container must be enlarged
        else:
            next_slot = self.rehash(hash_value)
            iters = 0
            while self.keys[next_slot] is not None and \
                    self.keys[next_slot] != key and \
                    iters <= len(self.keys):
                next_slot = self.rehash(next_slot)
                iters += 1

            if self.keys[next_slot] is None:
                self.keys[next_slot] = key
                self.values[next_slot] = value
            elif self.keys[next_slot] == key:
                self.values[next_slot] = value

    def get(self, key):
        iter_slot = self.calc_hash(key)
        value = None
        found = False
        iters = 0
        while not found and iters <= self.size:
            if self.keys[iter_slot] == key:
                found = True
                value = self.values[iter_slot]
            else:
                iter_slot = self.rehash(iter_slot)
                iters += 1
        return value

    def __getitem__(self, item):
        return self.get(item)

    def __setitem__(self, item, data):
        self.put(item, data)


if __name__ == '__main__':
    t = HashTable()
    t.put(10, 'some')
    t.put(23, 'other')
    t.put(33, 'words')
    t.put(46, 'might')
    t.put(52, 'be')
    t.put(64, 'more')
    t.put(79, 'appropriate')
    t.put(87, 'than')
    t.put(91, 'what')
    t.put(109, 'you say')
    print(t.keys)
    print(t.values)
    print(t.get((10)))
    print(t.get((30)))
    print(t[10])
    t[52] = 'otheressss'
    print(t[52])