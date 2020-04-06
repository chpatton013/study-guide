#!/usr/bin/env python3

import random
from typing import List

def insertionsort(l: List[int]):
    for i in range(1, len(l)):
        x = l[i]
        j = i
        while j > 0 and l[j - 1] > x:
            l[j] = l[j - 1]
            j -= 1
        l[j] = x


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
    insertionsort(actual)
    assert actual == expected, f"\nINPUT:\n{input}\nEXPECTED:\n{expected}\nACTUAL:\n{actual}"

insertionsort(random.sample(range(2147483647), k=100000))
