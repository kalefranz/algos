"""
22. Generate Parentheses
Medium

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

https://leetcode.com/problems/generate-parentheses/
"""
from collections import deque
import os.path
from typing import *

from lc.numbered import load_json


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        results = []

        def backtrack(S, left, right):
            if len(S) == 2 * n:
                results.append("".join(S))
                return
            if left < n:
                S.append("(")
                backtrack(S, left+1, right)
                S.pop()
            if right < left:
                S.append(")")
                backtrack(S, left, right+1)
                S.pop()

        backtrack([], 0, 0)
        return results


CASES = (
    (["()"], 1),
    (["(())", "()()"], 2),
    ([
         "(())()",
         "()(())",

         "((()))",
         "(()())",

         "()()()",
     ], 3),
    ([
        "()((()))",
        "(()(()))",
        "((()()))",
        "((())())",
        "((()))()",

        "()()(())",
        "()(()())",
        "()(())()",
        "(())()()",

        "(()(()))",
        "((()()))",
        "((())())",

        "(()()())",
        "(((())))",

        "()()()()",

        "(()())()",
        "(())(())",
     ], 4),
)
# 1 -> 1
# 2 -> 2
# 3 -> 5
# 4 -> 14
# 5 -> 42
# 6 -> 132

data = load_json(int(os.path.basename(__file__)[:-3]))
TEST_CALL = getattr(Solution(), list(Solution.__dict__.keys())[1])
def test(*test_nums):
    cases = test_nums and [CASES[num] for num in test_nums] or CASES

    failed = 0
    for q, (expected, *input_args) in enumerate(cases):
        result = TEST_CALL(*input_args)
        if set(result) == set(expected):
            print(f"{q}: passed")
        else:
            print(f"{q}: FAILED")
            print(set(result) - set(expected))
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
