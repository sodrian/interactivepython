#!/usr/bin/env python


def search_in_list(l, item):
    pos = 0
    found = False

    while pos < len(l) and not found:
        if l[pos] == item:
            found = True
        else:
            pos += 1

    return found


if __name__ == '__main__':
    print(search_in_list(range(10), 5))
    print(search_in_list(range(100000000), 5000))