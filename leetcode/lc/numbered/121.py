"""
121. Best Time to Buy and Sell Stock
Easy

You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a
different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit,
return 0.

https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

"""
from collections import deque
import os.path
from typing import *

from lc.numbered import load_json


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        miny, max_profit = float('inf'), 0
        for price in prices:
            max_profit = max(max_profit, price - miny)
            miny = min(miny, price)
        return max_profit

    def maxProfit_scratch(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        mins, maxs = [], []
        xmin, ymin = xmax, ymax = 0, prices[0]
        for q in range(1, len(prices)):
            if prices[q] < ymin:
                # careful here, need to ensure that xmin doesn't trample xmax
                if q > xmax:
                    mins.append((xmin, ymin))
                    maxs.append((xmax, ymax))
                    xmax, ymax = q, prices[q]
                xmin, ymin = q, prices[q]
            elif prices[q] > ymax:
                xmax, ymax = q, prices[q]

    def maxProfit_tooooo_slow(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        local_mins = []
        local_maxs = []
        slope_prev = -1000
        for q in range(1, len(prices)):
            slope = prices[q] - prices[q-1]
            if slope_prev <= 0 and slope >= 0:
                local_mins.append((q-1, prices[q-1]))
            elif slope_prev >= 0 and slope <= 0:
                local_maxs.append((q - 1, prices[q - 1]))
            slope_prev = slope
        if prices[-1] - prices[-2] >= 0:
            local_maxs.append((len(prices)-1, prices[-1]))

        pairs = []
        for xmin, ymin in local_mins:
            for xmax, ymax in local_maxs:
                if xmax <= xmin:
                    continue
                pair = (xmin, ymin), (xmax, ymax)
                pairs.append(pair)
        if not pairs:
            return 0
        greatest_diff_pair = max(pairs, key=lambda pair: pair[1][1]-pair[0][1])
        return greatest_diff_pair[1][1]-greatest_diff_pair[0][1]


TEST_CALL = getattr(Solution(), list(Solution.__dict__.keys())[1])
data = load_json(int(os.path.basename(__file__)[:-3]))
CASES = (
    # ## expected, *input_args
    (5, [7,1,5,3,6,4]),
    (0, [7,6,4,3,1]),
    (2, [2,4,1]),
    (0, [1]),
    (999, data["prices4"]),
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
