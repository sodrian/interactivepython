#!/usr/bin/env python
import copy
import random


def bubble_sort(l):
    assert isinstance(l, list), 'only lists are accepted as arguments'
    assert len(l) >= 2, 'list must have at least 2 elements'

    ops = 0
    for i in range(len(l)-1, 0, -1):
        for j in range(i):
            if l[j] > l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]
                ops += 1
    print('number of operations: {0}'.format(ops))


def short_bubble_sort(l):
    ops = 0
    n = len(l) - 1
    changes = True
    while n > 0 and changes:
        changes = False
        for i in range(n):
            if l[i] > l[i+1]:
                l[i], l[i+1] = l[i+1], l[i]
                changes = True
                ops += 1
        n -= 1
    print('number of operations: {0}'.format(ops))


if __name__ == '__main__':
    l1 = [random.randint(10, 100) for i in range(10)]
    l2 = copy.deepcopy(l1)

    print('bubble sort')
    print(l1)
    bubble_sort(l1)
    print(l1)
    print('')

    print('short bubble sort')
    print(l2)
    short_bubble_sort(l2)
    print(l2)