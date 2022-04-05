"""
10. Regular Expression Matching
Hard

Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:

    '.' Matches any single character.​​​​
    '*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).

https://leetcode.com/problems/regular-expression-matching/

Support characters [a-z] along with regex `.` and `*`
  - `.` matches any single character (i.e. [a-z])
  - `*` matches zero or more of the preceding character
  - `.*` matches zero or more of any character

"""
from collections import deque
from itertools import pairwise
import os.path
from typing import *

from lc.numbered import load_json


class Solution:
    def isMatch(self, strng: str, pattern: str) -> bool:
        return self.isMatch_copied_answer(strng, pattern)

    def isMatch_copied_answer(self, strng: str, pattern: str) -> bool:
        if not pattern:
            return not strng
        first_match = bool(strng) and pattern[0] in {strng[0], '.'}

        if len(pattern) >= 2 and pattern[1] == '*':
            return (self.isMatch(strng, pattern[2:]) or
                    first_match and self.isMatch(strng[1:], pattern))
        else:
            return first_match and self.isMatch(strng[1:], pattern[1:])

    def isMatch_bastards(self, strng: str, pattern: str) -> bool:
        def tokenize(pttrn: str):
            a = b = None
            for a, b in pairwise(pttrn):
                if b == "*":
                    yield a + b
                elif a == "*":
                    continue
                else:
                    yield a
            if b not in (None, "*"):
                yield b

        strng_idx = 0
        tokens = deque(tokenize(pattern))

        repeat = False
        try:
            while tokens:
                token = tokens.popleft()
                s = token[0]
                repeat = len(token) == 2
                if repeat:
                    if s == ".":
                        token_peak = tokens[0] if tokens else None
                        while strng[strng_idx].isalpha() and strng[strng_idx] != token_peak:  # could be an error here; could match none
                            strng_idx += 1
                    else:
                        while strng[strng_idx] == s:
                            strng_idx += 1
                else:
                    if s == ".":
                        assert strng[strng_idx].isalpha(), (strng, strng_idx, s)
                        strng_idx += 1
                    else:
                        assert strng[strng_idx] == s, (strng, strng_idx, s)
                        strng_idx += 1
            if strng_idx < len(strng):
                return False
        except IndexError:
            if tokens:
                return False
            if strng_idx == len(strng) and repeat:
                # if we went one over, and repeat is enabled, then we're ok
                return True
            return False
        except AssertionError:
            return False

        return True


data = load_json(int(os.path.basename(__file__)[:-3]))
CASES = (
    (True, "abcdefg", "a.c.efg"),
    (True, "abbbbc", "ab*c"),
    (False, "abbbbdc", "ab*c"),
    (False, "aa", "a"),
    (True, "aa", "a*"),
    (True, "ab", ".*"),
    (False, "ab", ".*c"),
    (True, "aaa", "a*a"),
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
