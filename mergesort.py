#!/usr/bin/env python3

import random
from typing import List

def _split_merge(l_scratch: List[int], begin: int, end: int, l_result: List[int]):
    if end - begin < 2:
        return
    middle = int(begin + (end - begin) / 2)
    _split_merge(l_result, begin, middle, l_scratch)
    _split_merge(l_result, middle, end, l_scratch)
    _merge(l_scratch, begin, middle, end, l_result)

def _merge(l_result: List[int], begin: int, middle: int, end: int, l_scratch: List[int]):
    lhs = begin
    rhs = middle
    for index in range(begin, end):
        if lhs < middle and (rhs >= end or l_result[lhs] < l_result[rhs]):
            l_scratch[index] = l_result[lhs]
            lhs += 1
        else:
            l_scratch[index] = l_result[rhs]
            rhs += 1

def mergesort(l: List[int]):
    l_scratch = l[:]
    _split_merge(l_scratch, 0, len(l), l)

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
    mergesort(actual)
    assert actual == expected, f"\nINPUT:\n{input}\nEXPECTED:\n{expected}\nACTUAL:\n{actual}"

mergesort(random.sample(range(2147483647), k=100000))
