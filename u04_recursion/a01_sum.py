#!/usr/bin/env python
import random


def recursive_sum(l):
    if len(l) == 1:
        return l[0]
    else:
        return l[0] + recursive_sum(l[1:])


if __name__ == '__main__':
    l = [random.randint(10, 100) for i in range(10)]
    print(l)
    print(recursive_sum(l))
