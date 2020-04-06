#!/usr/bin/env python3

from typing import List, Optional

def binary_search(v: int, l: List[int]) -> Optional[int]:
    lo = 0
    hi = len(l) - 1
    while lo <= hi:
        mid = int(lo + (hi - lo) / 2)
        if l[mid] < v:
            lo = mid + 1
        elif l[mid] > v:
            hi = mid - 1
        else:
            return mid
    return None

TEST_CASES = [
    ((3, []), None),
    ((3, [1,2,4,5]), None),
    ((3, [3]), 0),
    ((3, [3,3,3]), 1),
    ((3, [1,2,3,4,5]), 2),
]

for test_case in TEST_CASES:
    input = test_case[0]
    expected = test_case[1]
    actual = binary_search(*input)
    assert actual == expected, f"\nINPUT:\n{input}\nEXPECTED:\n{expected}\nACTUAL:\n{actual}"
