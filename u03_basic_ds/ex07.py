class Node(object):
    def __init__(self, data):
        self.next = None
        self.data = data


class LinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, item):
        node = Node(item)
        if not self.head:
            self.head = node
        elif not self.tail:
            self.head.next = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def pop(self):
        if not self.head:
            raise IndexError('list is empty')
        elif not self.tail:
            item = self.head
            self.head = None
        else:
            item = self.head
            self.head = item.next
        return item.data


class Queue(object):
    def __init__(self):
        self.c = LinkedList()

    def enqueue(self, item):
        self.c.add(item)

    def dequeue(self):
        return self.c.pop()

    def show(self):
        cur = self.c.head
        pr = ''
        while cur is not None:
            pr += '{0}{1}'.format(cur.data, cur.next and '->' or '')
            cur = cur.next
        print(pr)
