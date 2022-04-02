"""
13. Roman to Integer
Easy

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as
XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral
for four is not IIII. Instead, the number four is written as IV. Because the one is before the
five we subtract it making four. The same principle applies to the number nine, which is written
as IX. There are six instances where subtraction is used:

    I can be placed before V (5) and X (10) to make 4 and 9.
    X can be placed before L (50) and C (100) to make 40 and 90.
    C can be placed before D (500) and M (1000) to make 400 and 900.

Given a roman numeral, convert it to an integer.

https://leetcode.com/problems/roman-to-integer/

"""
from collections import deque
import os.path
from typing import *

from lc.numbered import load_json


numermap = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000,
}
subcuznext = {
    'I': {'V', 'X'},
    'X': {'L', 'C'},
    'C': {'D', 'M'},
}

class Solution:
    def romanToInt(self, s: str) -> int:
        total = 0
        queue = deque(s)
        while queue:
            c = queue.popleft()
            if c in subcuznext:
                if queue and queue[0] in subcuznext[c]:
                    total -= numermap[c]
                    continue
            total += numermap[c]
        return total


data = load_json(int(os.path.basename(__file__)[:-3]))
CASES = (
    (3, "III"),
    (44, "XLIV"),
    (58, "LVIII"),
    (1994, "MCMXCIV"),
    (1, "I"),
    (5, "V"),
    (4, "IV"),
)
TEST_CALL = getattr(Solution(), list(Solution.__dict__.keys())[1])
def test(*test_nums):
    cases = test_nums and [CASES[num] for num in test_nums] or CASES

    failed = 0
    for q, (expected, *input_args) in enumerate(cases):
        result = TEST_CALL(*input_args)
        if result == expected:
            print(f"{q}: passed")
        else:
            print(f"{q}: FAILED")
            print(f"  {expected} != {result}")
            failed += 1
    if failed:
        print(f"FAILED: {failed}")
    else:
        print(f"SUCCESS: TESTS PASSED == {len(cases)}")

    return failed


if __name__ == "__main__":
    import sys
    sys.exit(test())
