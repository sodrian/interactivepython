#!/usr/bin/env python


def reverse_str(s):
    if len(s) <= 1:
        return s
    else:
        return s[-1] + reverse_str(s[:-1])


if __name__ == '__main__':
    print(reverse_str('some'))
    print(reverse_str('this is sparta'))
    print(reverse_str('some other words'))
    print(reverse_str(''))