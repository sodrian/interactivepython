#!/usr/bin/env python
import random


class Stack(object):
    def __init__(self):
        self.cont = []

    def __len__(self):
        return len(self.cont)

    def push(self, item):
        self.cont.append(item)

    def pop(self):
        return self.cont.pop()

    def peek(self):
        try:
            return self.cont[-1]
        except IndexError:
            raise IndexError('Stack is empty')

    def size(self):
        return len(self)

    def is_empty(self):
        return len(self) == 0


class Stack2(object):
    """pop and push in this variation have O(n) complexity
    Not recommended to use for big stacks
    """

    def __init__(self):
        self.cont = []

    def __len__(self):
        return len(self.cont)

    def push(self, item):
        self.cont.insert(0, item)

    def pop(self):
        return self.cont.pop(0)

    def peek(self):
        try:
            return self.cont[0]
        except IndexError:
            raise IndexError('Stack is empty')

    def size(self):
        return len(self)

    def is_empty(self):
        return len(self) == 0


class BalancedString(object):
    def __init__(self, s):
        assert isinstance(s, str), 'please provide string argument'
        self.s = s

    def check(self):
        balanced = True
        stack = Stack()
        for i in self.s:
            if i == '(':
                stack.push(i)
            if i == ')':
                try:
                    stack.pop()
                except IndexError:
                    balanced = False
                    break
        return balanced and stack.is_empty()


class BalancedStringAll(object):
    OPENING_BRACKETS = '([{'
    CLOSING_BRACKETS = ')]}'

    def __init__(self, s):
        assert isinstance(s, str), 'please provide string argument'
        self.s = s

    def is_opening_bracket(self, el):
        return el in self.OPENING_BRACKETS

    def is_closing_bracket(self, el):
        return el in self.CLOSING_BRACKETS

    def brackets_match(self, b1, b2):
        return self.OPENING_BRACKETS.index(b1) == self.CLOSING_BRACKETS.index(b2)

    def check(self):
        balanced = True
        stack = Stack()
        for substr in self.s:
            if self.is_opening_bracket(substr):
                stack.push(substr)
            elif self.is_closing_bracket(substr):
                if stack.is_empty() or not self.brackets_match(stack.peek(), substr):
                    balanced = False
                    break
                else:
                    stack.pop()
        return balanced and stack.is_empty()


def divive_by_two(number):
    assert isinstance(number, int), 'please provice integer'
    stack = Stack()
    while number:
        rem = number % 2
        number //= 2
        stack.push(rem)
    bin_str = ''
    while not stack.is_empty():
        bin_str += str(stack.pop())
    return bin_str


def convert_to_base(number, base):
    DIGITS = '0123456789ABCDEFGIJKLMNOPQRSTUVWXYZ'
    assert isinstance(number, int), 'number must be integer'
    assert isinstance(base, int), 'base must be integer'
    assert base in range(2, 37), 'base must be in [2, 36] range'

    s = Stack()
    while number > 0:
        rem = number % base
        number //= base
        s.push(rem)

    out = ''
    while not s.is_empty():
        out += str(DIGITS[s.pop()])

    return out


if __name__ == '__main__':
    n = 10
    digits = random.sample(range(10000), n)
    bases = random.sample(range(2, 20), n)

    for i in xrange(1, n):
        print('{0} with base {1} is {2}'.format(
            digits[i],
            bases[i],
            convert_to_base(digits[i], bases[i])))
