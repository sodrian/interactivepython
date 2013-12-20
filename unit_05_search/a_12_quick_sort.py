import random


def quick_sort_basic(lst):
    if len(lst) == 0:
        return []
    else:
        pivot = lst[0]
        lesser = quick_sort_basic([x for x in lst[1:] if x < pivot])
        greater = quick_sort_basic([x for x in lst[1:] if x > pivot])

        return lesser + [pivot] + greater


def quick_sort_partition(lst):
    quick_sort_helper(lst, 0, len(lst)-1)


def quick_sort_helper(lst, first, last):
    if first < last:
        split_point = partition(lst, first, last)
        quick_sort_helper(lst, first, split_point-1)
        quick_sort_helper(lst, split_point+1, last)


def partition(lst, first, last):
    pivot_value = lst[first]
    left_mark = first + 1
    right_mark = last

    exit = False
    while not exit:
        while left_mark <= right_mark and lst[left_mark] <= pivot_value:
            left_mark += 1
        while right_mark >= left_mark and lst[right_mark] >= pivot_value:
            right_mark -= 1

        if right_mark < left_mark:
            exit = True
        else:
            lst[left_mark], lst[right_mark] = lst[right_mark], lst[left_mark]

    lst[first], lst[right_mark] = lst[right_mark], lst[first]

    return right_mark



l = random.sample(range(1000), 10)
print(l)
quick_sort_partition(l)
print(l)

