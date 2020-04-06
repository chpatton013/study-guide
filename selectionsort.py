#!/usr/bin/env python3

import random
from typing import List

def selectionsort(l: List[int]):
    for i in range(len(l) - 1):
        min_j = i
        for j in range(i + 1, len(l)):
            if l[j] < l[min_j]:
                min_j = j
        l[i], l[min_j] = l[min_j], l[i]


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
    selectionsort(actual)
    assert actual == expected, f"\nINPUT:\n{input}\nEXPECTED:\n{expected}\nACTUAL:\n{actual}"

selectionsort(random.sample(range(2147483647), k=100000))
