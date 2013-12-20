def search_in_list(l, item):
    pos = 0
    found = False

    while pos < len(l) and not found:
        if l[pos] == item:
            found = True
        else:
            pos += 1

    return found

print(search_in_list(range(10), 5))
print(search_in_list(range(100000000), 5000))