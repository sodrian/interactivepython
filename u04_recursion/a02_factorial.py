#!/usr/bin/env python


def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)


if __name__ == '__main__':
    for i in range(10):
        print(factorial(i))
