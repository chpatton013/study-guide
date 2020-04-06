#!/usr/bin/env python3

import random
from typing import List

def _partition(l: List[int], begin: int, end: int, mask: int):
    while begin < end:
        if l[begin] & mask:
            l[begin], l[end - 1] = l[end - 1], l[begin]
            end -= 1
        else:
            begin += 1
    return begin

def _radixsort(l: List[int], begin: int, end: int, mask: int):
    if end - begin <= 1 or not mask:
        return
    pivot = _partition(l, begin, end, mask)
    _radixsort(l, begin, pivot, mask >> 1)
    _radixsort(l, pivot, end, mask >> 1)

def radixsort(l: List[int]):
    _radixsort(l, 0, len(l), 1 << 32)

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
    radixsort(actual)
    assert actual == expected, f"\nINPUT:\n{input}\nEXPECTED:\n{expected}\nACTUAL:\n{actual}"

radixsort(random.sample(range(2147483647), k=100000))
