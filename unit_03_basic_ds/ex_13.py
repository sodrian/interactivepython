class Node(object):
    def __init__(self, item):
        self.data = item
        self.next = None


class UnorderedList(object):
    """def length(self) -> 0(1)
    """

    def __init__(self):
        self.head = None
        self.length = 0

    def add(self, item):
        node = Node(item)
        if self.length == 0:
            self.head = node
        else:
            cur = self.head
            while cur and cur.next:
                cur = cur.next
            cur.next = node
        self.length += 1

    def pop(self):
        if self.length == 0:
            raise IndexError('List is empty')
        elif self.length == 1:
            ret = self.head
            self.head = None
            self.length -= 1
            return ret.data
        else:
            cur = self.head
            prev = None
            while cur and cur.next:
                prev = cur
                cur = cur.next
            prev.next = None
            self.length -= 1
            return cur.data

    def show(self):
        s = ''
        cur = self.head
        while cur is not None:
            s += '{0}{1}'.format(cur.data, cur.next and '->' or '')
            cur = cur.next
        return s

    def __str__(self):
        return self.show()
