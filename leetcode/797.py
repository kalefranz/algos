"""
797. All Paths From Source to Target
Medium

Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, find all possible paths from node 0 to node n - 1 and return them in any order.

The graph is given as follows: graph[i] is a list of all nodes you can visit from node i (i.e., there is a directed edge from node i to node graph[i][j]).


"""
from collections import deque
from itertools import zip_longest
from pprint import pformat, pprint
from textwrap import indent
from typing import *


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        def chain(vertex):
            stack = []
            stack.append([vertex])
            while stack:
                children = graph[stack[-1][-1]]
                if children:
                    stack.append(list(children))
                else:
                    # dump last element of entire stack, and then back up to next available branch
                    c = [s[-1] for s in stack]
                    yield c
                    while stack:
                        if len(stack[-1]) > 1:
                            stack[-1].pop()
                            break
                        else:
                            stack.pop()
        return list(chain(0))


TEST_CALL = Solution().allPathsSourceTarget
CASES = (
    # ## expected, *input_args
    ([[0,1,3],[0,2,3]], [[1,2],[3],[3],[]]),
    ([[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]], [[4,3,1],[3,2,4],[3],[4],[]]),
    (
        [[0,3,6,7],[0,3,4,7],[0,3,4,6,7],[0,3,4,5,6,7],[0,1,4,7],[0,1,4,6,7],[0,1,4,5,6,7],[0,1,6,7],[0,1,7],[0,1,2,4,7],[0,1,2,4,6,7],[0,1,2,4,5,6,7],[0,1,2,6,7],[0,1,2,3,6,7],[0,1,2,3,4,7],[0,1,2,3,4,6,7],[0,1,2,3,4,5,6,7],[0,1,5,6,7]],
        [[3,1],[4,6,7,2,5],[4,6,3],[6,4],[7,6,5],[6],[7],[]],
    ),
    (
        [[0,4],[0,3,4],[0,1,3,4],[0,1,4]],
        [[4,3,1],[3,2,4],[],[4],[]],
    ),
)
def test(*test_nums):
    cases = test_nums and [CASES[num] for num in test_nums] or CASES

    failed = 0
    for q, (expected, *input_args) in enumerate(cases):
        result = TEST_CALL(*input_args)
        pprint(result)
        result = list(sorted(set(map(tuple, result))))
        expected = list(sorted(set(map(tuple, expected))))

        if result == expected:
            print(f"{q}: passed")
        else:
            print(f"{q}: FAILED")
            failed += 1
        print(input_args[0])
        print("  {0:^25}    {1:^25}".format("expected:", "result:"))
        print("\n".join(f"  {str(e):>25}    {str(r):>25}" for e, r in zip_longest(expected, result)))

    if failed:
        print(f"FAILED: {failed}")
    else:
        print(f"SUCCESS: TESTS PASSED == {len(cases)}")
test(3)
