"""
997. Find the Town Judge
Easy

In a town, there are n people labeled from 1 to n. There is a rumor that one of these people is secretly the town judge.

If the town judge exists, then:

    The town judge trusts nobody.
    Everybody (except for the town judge) trusts the town judge.
    There is exactly one person that satisfies properties 1 and 2.

You are given an array trust where trust[i] = [ai, bi] representing that the person labeled ai trusts the person labeled bi.

Return the label of the town judge if the town judge exists and can be identified, or return -1 otherwise.

https://leetcode.com/problems/find-the-town-judge/
"""
from collections import defaultdict, deque
import os.path
from typing import *

from lc.numbered import load_json


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trusts_count = [0] * n
        trusted_by_count = [0] * n
        for a_trusts_b in trust:
            a, b = a_trusts_b
            trusts_count[a-1] += 1
            trusted_by_count[b-1] += 1
        try:
            n = trusted_by_count.index(n-1) + 1
        except ValueError:
            return -1
        if trusts_count[n-1] == 0:
            return n
        return -1


TEST_CALL = getattr(Solution(), list(Solution.__dict__.keys())[1])
data = load_json(int(os.path.basename(__file__)[:-3]))
CASES = (
    # ## expected, *input_args
    (2, 2, [[1,2]]),
    (3, 3, [[1,3],[2,3]]),
    (-1, 3, [[1,3],[2,3],[3,1]]),
    (3, 4, [[1,3],[1,4],[2,3],[2,4],[4,3]]),
    (-1, 3, [[1,2],[2,3]]),
)
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
