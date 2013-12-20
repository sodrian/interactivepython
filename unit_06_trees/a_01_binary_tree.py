class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def assign_left(self, value):
        self.left = value

    def assign_right(self, value):
        self.right = value



t = Node(4)
t.assign_left(Node(2))
t.assign_right(Node(7))
print(t)