"""
17. Letter Combinations of a Phone Number
Medium

Given a string containing digits from 2-9 inclusive, return all possible letter combinations that
the number could represent. Return the answer in any order.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1
does not map to any letters.

"""
from collections import deque
import os.path
from typing import *

from lc.numbered import load_json


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        results = []
        digmap = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz",
        }

        def backtrack(digs, letters):
            if not digs:
                if letters:
                    results.append(letters)
                return
            ltrs = digmap[digs[0]]
            for ltr in ltrs:
                backtrack(digs[1:], letters+ltr)

        backtrack(digits, "")
        return results


data = load_json(int(os.path.basename(__file__)[:-3]))
CASES = (
    (["ad","ae","af","bd","be","bf","cd","ce","cf"], "23"),
    ([], ""),
    (["a","b","c"], "2"),
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
