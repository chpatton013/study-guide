#!/usr/bin/env python3

import random
from typing import List

def bubblesort(l: List[int]):
    for i in range(len(l)):
        for j in range(0, len(l) - i - 1):
            if l[j] > l[j + 1]:
                l[j], l[j + 1] = l[j + 1], l[j]

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
    bubblesort(actual)
    assert actual == expected, f"\nINPUT:\n{input}\nEXPECTED:\n{expected}\nACTUAL:\n{actual}"

bubblesort(random.sample(range(2147483647), k=100000))
