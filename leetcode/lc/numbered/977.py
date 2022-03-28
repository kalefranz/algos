class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result = []
        stack = []
        for n in nums:
            if n < 0:
                stack.append(n*n)
            else:
                n *= n
                while stack and n > stack[-1]:
                    result.append(stack.pop())
                result.append(n)
        result.extend(reversed(stack))
        return result

    return failed


if __name__ == "__main__":
    import sys
    sys.exit(test())

