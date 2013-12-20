class Node(object):
    def __init__(self, item):
        self.data = item
        self.next = None


class UnorderedList(object):
    def __init__(self):
        self.head = None

    def add(self, item):
        node = Node(item)
        cur = self.head
        while cur and cur.next:
            cur = cur.next

        if cur is None:
            self.head = node
        else:
            cur.next = node

    def __str__(self):
        s = '['
        cur = self.head
        while cur is not None:
            s += "'{0}'{1}".format(cur.data, cur.next and ',' or '')
            cur = cur.next
        s += ']'
        return s

l = UnorderedList()
l.add('some')
print(l)
l.add('print')
print(l)
l.add('something else')
print(l)
