#!/usr/bin/env python
import random


def selection_sort(l):
    assert isinstance(l, list)
    assert len(l) >= 2

    for i in range(len(l)-1, 0, -1):
        maximum_pos = 0
        for j in range(i):
            if l[j] > l[maximum_pos]:
                maximum_pos = j
        l[maximum_pos], l[i] = l[i], l[maximum_pos]


if __name__ == '__main__':
    l = [random.randint(10, 100) for i in range(10)]
    print(l)
    selection_sort(l)
    print(l)