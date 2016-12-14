#!/usr/bin/env python


def hash_func(string, t_size):
    s = 0
    for i in string:
        s += ord(i)
    return s % t_size


if __name__ == '__main__':
    print(hash_func('some', 15))