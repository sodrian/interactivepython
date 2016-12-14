#!/usr/bin/env python


def check_is_palindrome(s):
    if len(s) <= 1:
        return True
    else:
        return s[0] == s[-1] and check_is_palindrome(s[1:-1])


if __name__ == '__main__':
    words = ['kayak', 'some', 'other']

    for w in words:
        print('{0} -> {1}'.format(w, check_is_palindrome(w)))
