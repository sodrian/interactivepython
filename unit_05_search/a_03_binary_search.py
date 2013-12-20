def vis_print(length, first, mid, last):
    print('-'*length)
    print(' '*first + '|' +
          ' '*(first<=mid-1 and mid-first-1 or 0) + '|' +
          ' '*(mid<=last-2 and last-mid-2 or 0) + '|')
    print('-'*length)
    print(' ')
    print(' ')


def binary_search(l, item):
    found = False
    first = 0
    last = len(l) - 1
    length = len(l)
    while first <= last and not found:
        midpoint = (first + last) // 2
        vis_print(length, first, midpoint, last)
        if l[midpoint] == item:
            found = True
        elif item < l[midpoint]:
            last = midpoint - 1
        else:
            first = midpoint + 1

    return found

print(binary_search(range(100), 20))
print(binary_search(range(100), 0))
print(binary_search(range(100), 1000))