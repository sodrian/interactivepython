#!/usr/bin/env python


def conv_to_base(number, base):
    s = '0123456789ABCDEFGHIJ'
    assert base <= len(s), 'the provided base is too long'
    if number < base:
        return s[number]
    else:
        return conv_to_base(number // base, base) + s[number % base]


if __name__ == '__main__':
    print(conv_to_base(17, 16))
    print(conv_to_base(30, 16))
    print(conv_to_base(170, 16))
    print(conv_to_base(3550, 16))
    print(conv_to_base(10, 2))
    print(conv_to_base(10, 17))