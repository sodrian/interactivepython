import random


def insertion_sort(l):
    assert isinstance(l, list)
    assert len(l) >= 2

    for i in range(1, len(l)):
        val = l[i]
        j = i
        while j > 0 and l[j-1] > val:
            l[j] = l[j-1]
            j -= 1
        l[j] = val

l = random.sample(range(1000), 20)
print(l)
insertion_sort(l)
print(l)