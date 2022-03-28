"""
150. Evaluate Reverse Polish Notation
Medium

Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, and /. Each operand may be an integer or another expression.

Note that division between two integers should truncate toward zero.

It is guaranteed that the given RPN expression is always valid. That means the expression would always evaluate to a result, and there will not be any division by zero operation.

"""
from collections import deque
from functools import reduce
from typing import *

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {
            '+': lambda x,y: x+y,
            '*': lambda x,y: x*y,
            '-': lambda x,y: y-x,
            '/': lambda x,y: int(y/x),
        }
        stack = deque()
        for t in tokens:
            if t in operators:
                stack.append(operators[t](stack.pop(), stack.pop()))
            else:
                stack.append(int(t))
        return stack.pop()


TEST_CALL = Solution().evalRPN
CASES = (
    ## expected, *input_args
    (9, ["2","1","+","3","*"]),
    (6, ["4","13","5","/","+"]),
    (22, ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]),
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
test()

    return failed


if __name__ == "__main__":
    import sys
    sys.exit(test())

