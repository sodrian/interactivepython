def ordered_sequential_search(l, item):
    l = list(l)
    pos = 0
    found = False
    stop = False

    while pos < len(l) and not found and not stop:
        if l[pos] == item:
            found = True
        elif l[pos] > item:
            stop = True
        else:
            pos += 1

    return found

print(ordered_sequential_search(range(10), 5))
print(ordered_sequential_search(range(0, 100, 5), 4))