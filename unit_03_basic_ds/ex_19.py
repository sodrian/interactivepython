class Node(object):
    def __init__(self, item):
        self.data = item
        self.next = None


class UnorderedLinkedList(object):
    def __init__(self):
        self.head = None
        self.length = 0

    def __str__(self):
        s = '['
        cur = self.head
        while cur is not None:
            s += "'{0}'{1}".format(cur.data, cur.next and ',' or '')
            cur = cur.next
        s += ']'
        return s

    def add(self, item):
        node = Node(item)
        if self.head is None:
            self.head = node
        else:
            cur = self.head
            while cur and cur.next:
                cur = cur.next
            cur.next = node
        self.length += 1

    def remove(self, item):
        pass

    def slice(self, start, stop):
        assert isinstance(start, int), 'start must be integer'
        assert isinstance(stop, int), 'stop must be integer'
        assert start in range(self.length+1), 'start is out of list\'s range'
        assert stop in range(self.length+1), 'stop is out of list\'s range'
        assert start != stop, 'start can not be equal to stop'
        assert start < stop, 'start must be less than stop'

        ret_list = UnorderedLinkedList()

        cur = self.head
        snd_cur = ret_list.head
        cur_pos = 0

        while cur:
            if cur_pos == start:
                ret_list.head = Node(cur.data)
                snd_cur = ret_list.head
            elif start < cur_pos < stop:
                snd_cur.next = Node(cur.data)
                snd_cur = snd_cur.next
            elif cur_pos == stop:
                break
            cur = cur.next
            cur_pos += 1
        return ret_list

l = UnorderedLinkedList()
l.add('some')
l.add('print')
l.add('this')
l.add('alson')
print(l)
print(l.slice(0,1))
print(l.slice(0,2))
print(l.slice(3,4))
