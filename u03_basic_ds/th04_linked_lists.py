#!/usr/bin/env python


class Node(object):
    def __init__(self, data):
        assert data is not None, 'data must be not None'
        self.data = data
        self.next = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_data(self, data):
        self.data = data

    def set_next(self, n):
        self.next = n

    def __repr__(self):
        return(str(self.data))

    def __str__(self):
        return(str(self.data))


class LinkedList(object):
    def __init__(self):
        self.head = None

    def show_list(self):
        cur = self.head
        out = ''
        while cur is not None:
            out += '{0}{1}'.format(cur.data, cur.next and '->' or '')
            cur = cur.next
        print(out)


class UnorderedList(LinkedList):
    def __iter__(self):
        cur = self.head
        while cur is not None:
            yield cur
            cur = cur.next
        return

    def add(self, item):
        tmp = Node(item)
        tmp.next = self.head
        self.head = tmp

    def append(self, item):
        cur = self.head
        while cur is not None:
            if cur.next is None:
                break
            cur = cur.next
        tmp = Node(item)
        cur.next = tmp

    def length(self):
        l = 0
        for _ in self:
            l += 1
        return l

    def search_by_iter(self, item):
        found = False
        for cur in self:
            if item == cur.data:
                found = True
                break
        return found

    def search(self, item):
        found = False
        cur = self.head
        while cur is not None and not found:
            if cur.get_data() == item:
                found = True
            else:
                cur = cur.next
        return found

    def remove(self, item):
        cur = self.head
        prev = None
        found = False

        while cur is not None and not found:
            if item == cur.data:
                found = True
            else:
                prev = cur
                cur = cur.next

        if found:
            if prev is None:
                self.head = cur.next
            else:
                prev.next = cur.next

    def is_empty(self):
        return self.head == None

    def index(self, item):
        cur = self.head
        count = 0
        found = False
        while cur is not None and not found:
            if cur.data == item:
                found = True
                break
            cur = cur.next
            count += 1

        return found and count or None

    def insert(self, pos, item):
        cur = self.head
        prev = None
        inserted = False
        count = 0
        while cur is not None and not inserted:
            if count == pos:
                inserted = True
                tmp = Node(item)
                tmp.next = cur
                if prev:
                    prev.next = tmp
                else:
                    self.head = tmp
            prev = cur
            cur = cur.next
            count += 1
        else:
            if count == pos:
                tmp = Node(item)
                self.head = tmp

    def pop(self, pop=None):
        pass



class OrderedList(LinkedList):
    def add(self, item):
        assert isinstance(item, (int, float)), \
            'only integers and floats are accepted'

        cur = self.head
        prev = None
        stop = False

        while cur is not None and not stop:
            if cur.data > item:
                stop = True
            else:
                prev = cur
                cur = cur.next

        tmp = Node(item)
        if prev is None:
            tmp.next = self.head
            self.head = tmp
        else:
            tmp.next = cur
            prev.next = tmp

    def remove(self, item):
        cur = self.head
        prev = None
        found = False

        while cur is not None and not found:
            if cur.data == item:
                found = True
            else:
                prev = cur
                cur = cur.next

        if found:
            if prev is None:
                self.head = self.head.next
            else:
                prev.next = cur.next

    def search(self, item):
        cur = self.head
        found = False
        while cur is not None and not found:
            if cur.data == item:
                found = True
            else:
                cur = cur.next
        return found

    def is_empty(self):
        return self.head == None

    def length(self):
        l = 0
        cur = self.head
        while cur is not None:
            l += 1
            cur = cur.next
        return l

    def index(self, item):
        ind = 0
        cur = self.head
        found = False
        while cur is not None and not found:
            if cur.data == item:
                found = True
            else:
                ind += 1
                cur = cur.next

        if found:
            return ind
        else:
            return None

    def pop(self, pos=None):
        cur = self.head
        prev = None
        found = False
        cur_p = 0
        while cur is not None and not found:
            if (isinstance(pos, int) and pos >= 0 and pos == cur_p) or \
                    cur.next is None:
                found = True
            else:
                cur_p += 1
                prev = cur
                cur = cur.next
        if found:
            if prev is None:
                self.head = cur.next
            else:
                prev.next = cur.next
            return cur
        else:
            raise IndexError('No item found with given position')


if __name__ == '__main__':
    l = UnorderedList()
    l.add(1)
    l.add('some')
    l.add('some3')
    l.add('4')
    l.add(5)
    l.add(True)
    l.show_list()
    l.append('some more')
    l.show_list()
    l.length()
