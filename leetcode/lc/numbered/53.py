class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best_sum = float('-inf')
        current_sum = 0
        for x in nums:
            current_sum = max(x, x+current_sum)
            best_sum = max(best_sum, current_sum)
        return best_sum            

    return failed


if __name__ == "__main__":
    import sys
    sys.exit(test())

