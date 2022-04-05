"""
5. Longest Palindromic Substring
Medium

Given a string s, return the longest palindromic substring in s.

https://leetcode.com/problems/longest-palindromic-substring/

"""
from collections import deque
import os.path
from typing import *

from lc.numbered import load_json


class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand_around_center(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return right - left - 1

        longest = 0
        pair = 0, 0
        for q in range(len(s)-1):
            a = expand_around_center(q, q)
            b = expand_around_center(q, q+1)
            l = max(a, b)
            if l > longest:
                longest = l
                pair = q - (l - 1) // 2, q + l // 2

        return s[pair[0]:pair[1]+1]

    def longestPalindrome_1(self, s: str) -> str:
        r = s[::-1]
        for j in range(len(r)-1,-1,-1):
            for k in range(len(r)-j):
                t = r[k:k+j+1]
                if t in s and t == t[::-1]:
                    return t

    def longestPalindrome_2(self, s: str) -> str:
        r = s[::-1]
        return next((
            r[k:k+j+1]
            for j in range(len(r) - 1, -1, -1)
            for k in range(len(r)-j)
            if r[k:k+j+1] in s and r[k:k+j+1] == r[k:k+j+1][::-1]
        ), None)

    def longestPalindrome_3(self, s: str) -> str:
        r = s[::-1]
        return next((
            t
            for j in range(len(r) - 1, -1, -1)
            for k in range(len(r)-j)
            if (t := r[k:k+j+1]) in s and t == t[::-1]
        ), None)



data = load_json(int(os.path.basename(__file__)[:-3]))
CASES = (
    ("bab", "babad"),
    ("bb", "cbbd"),
    ("defed", "abcdefeda"),
    ("a", "a"),
    ("aca", "aacabdkacaa"),
    (data["a4"], data["q4"]),
    ("jtotj", data["q5"]),
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
