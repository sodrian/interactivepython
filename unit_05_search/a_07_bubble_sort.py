import random


def bubble_sort(l):
    assert isinstance(l, list), 'only lists are accepted as arguments'
    assert len(l) >= 2, 'list must have at least 2 elements'
    ops = 0
    for i in range(len(l)-1, 0, -1):
        for j in range(i):
            if l[j] > l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]
                ops += 1
    print(ops)


def short_bubble_sort(l):
    ops = 0
    n = len(l) - 1
    changes = True
    while n > 0 and changes:
        changes = False
        for i in range(n):
            if l[i] > l[i+1]:
                l[i], l[i+1] = l[i+1], l[i]
                changes = True
                ops += 1
        n -= 1
    print(ops)


print('bubble sort')
l = [random.randint(10, 100) for i in range(10)]
print(l)
bubble_sort(l)
print(l)

print('\nshort bubble sort')
l = [10, 20, 30, 40, 90, 50, 60, 70, 80, 100]
print(l)
short_bubble_sort(l)
print(l)