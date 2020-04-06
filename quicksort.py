#!/usr/bin/env python3

import random
from typing import List, Optional

def _partition(l: List[int], begin: int, end: int):
    pivot = random.randrange(begin, end)
    l[end - 1], l[pivot] = l[pivot], l[end - 1]
    pivot = end - 1
    end = pivot

    while begin < end:
        if l[begin] < l[pivot]:
            begin += 1
        elif l[pivot] < l[end - 1]:
            end -= 1
        else:
            l[begin], l[end - 1] = l[end - 1], l[begin]
            end -= 1

    l[pivot], l[end] = l[end], l[pivot]
    return end

def _quicksort(l: List[int], begin: int, end: int):
    if begin < end - 1:
        pivot = _partition(l, begin, end)
        _quicksort(l, begin, pivot)
        _quicksort(l, pivot + 1, end)

def quicksort(l: List[int]):
    _quicksort(l, 0, len(l))

TEST_CASES = [
    ([], []),
    ([1], [1]),
    ([1,2,3], [1,2,3]),
    ([3,2,1], [1,2,3]),
    ([6,9,7,3,4,1,5,8,2], [1,2,3,4,5,6,7,8,9]),
]

for test_case in TEST_CASES:
    input = test_case[0]
    actual = input[:]
    expected = test_case[1]
    quicksort(actual)
    assert actual == expected, f"\nINPUT:\n{input}\nEXPECTED:\n{expected}\nACTUAL:\n{actual}"

quicksort(random.sample(range(2147483647), k=100000))
