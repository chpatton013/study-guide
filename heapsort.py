#!/usr/bin/env python3

import random
from typing import List

def _parent(index: int):
    return int((index - 1) / 2)

def _left_child(index: int):
    return index * 2 + 1

def _right_child(index: int):
    return index * 2 + 2

def _sift(l: List[int], begin: int, end: int):
    root = begin
    while _left_child(root) < end:
        swap = root

        left_child = _left_child(root)
        right_child = _right_child(root)

        if l[swap] < l[left_child]:
            swap = left_child
        if right_child < end and l[swap] < l[right_child]:
            swap = right_child
        if swap == root:
            break

        l[root], l[swap] = l[swap], l[root]
        root = swap

def _heapify(l: List[int]):
    index = _parent(len(l) - 1)
    while index >= 0:
        _sift(l, index, len(l))
        index -= 1

def heapsort(l: List[int]):
    _heapify(l)
    length = len(l)
    while length > 1:
        l[0], l[length - 1] = l[length - 1], l[0]
        length -= 1
        _sift(l, 0, length)

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
    heapsort(actual)
    assert actual == expected, f"\nINPUT:\n{input}\nEXPECTED:\n{expected}\nACTUAL:\n{actual}"

heapsort(random.sample(range(2147483647), k=100000))
