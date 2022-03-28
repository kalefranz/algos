from typing import *

def twoSum(numbers: List[int], target: int) -> List[int]:
    i = 0
    j = end = len(numbers) - 1

    # if too big, subtract one from j
    # if too small, add one to i
    # i != j
    def get_next(i, j):
        val = numbers[i] + numbers[j]
        assert val != target, val
        if val > target:
            if j > 0:
                j -= 1
            else:
                assert i > 0, i
                i -= 1
            assert i != j, (i, j)
        else:
            if i < end:
                i += 1
            else:
                assert j < end, j
                j += 1
            assert i != j, (i, j)
        return i, j

    q = 0
    while True:
        if numbers[i] + numbers[j] == target:
            break
        if q > end*end:
            assert False
        i, j = get_next(i, j)
        q += 1
        print(f"   {q} [{i+1},{j+1}] {target} ?= {numbers[i]+numbers[j]}")

    return [i+1, j+1]




inputs = (
    ([2,7,11,15], 9, [1,2]),
    ([2,3,4], 6, [1,3]),
    ([-1,0], -1, [1,2]),
)
for q, (nums, targ, expected) in enumerate(inputs):
    result = twoSum(nums, targ)
    print(f"{q} {expected == result}  {expected}  {result}")

    return failed


if __name__ == "__main__":
    import sys
    sys.exit(test())

