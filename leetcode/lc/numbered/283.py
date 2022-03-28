from typing import *

def move_zeroes_1(nums: List[int]) -> None:
    def swap(a, b):
        nums[a], nums[b] = nums[b], nums[a]

    for q in range(len(nums)-1-1, -1, -1):
        if nums[q] == 0:
            for p in range(q, len(nums)-1):
                if nums[p+1] == 0:
                    break
                swap(p, p+1)


from typing import *

def move_zeroes_1(nums: List[int]) -> None:
    def swap(a, b):
        nums[a], nums[b] = nums[b], nums[a]

    for q in range(len(nums)-1-1, -1, -1):
        if nums[q] == 0:
            for p in range(q, len(nums)-1):
                if nums[p+1] == 0:
                    break
                swap(p, p+1)


def move_zeroes_2(nums: List[int]) -> None:
    def shift(a, b):
        # a: index of zero
        # b: index of last non-zero, where a will go
        print(f"shifting ... nums[{a}:{b}], nums[{b}] = nums[{a+1}:{b+1}], nums[{a}]")
        nums[a:b], nums[b] = nums[a+1:b+1], nums[a]

    moved = -1
    last_moved = None
    for q in range(len(nums)-1-1, -1, -1):
        if nums[q] == 0:
            # q must be < (len(nums)-1) - (moved+1)
            # q + 2 < len(nums) - moved
            # q + 2 - len(nums) < - moved
            # moved > len(nums) - q - 2
            moved += 1
            last_moved = len(nums)-1 - moved
            while nums[last_moved] == 0 and last_moved > q+1:
                moved += 1
                last_moved = len(nums)-1 - moved
            # if nums[last_moved] == 0:
            #     assert q + 1 == last_moved, (q, last_moved)
            # else:
            if nums[last_moved] != 0:
                shift(q, last_moved)

        # print(q, last_moved, moved, nums)



def move_zeroes(nums: List[int]) -> None:
    lng = len(nums)
    nums[:] = [n for n in nums if n != 0]
    nums.extend(0 for _ in range(lng - len(nums)))




inputs = (
    ([0,1,0,3,12], [1,3,12,0,0]),
    ([0], [0]),
    ([1], [1]),
    ([0,1], [1,0]),
    ([1,0], [1,0]),
    ([1,1], [1,1]),
    ([0,0], [0,0]),

    ([0, 0, 0, 3, 4, 5, 0, 7, 8, 0, 10, 0, 12, 13], [3,4,5,7,8,10,12,13,0,0,0,0,0,0]),
    ([0, 0, 0, 3, 4, 5, 0, 7, 8, 0, 10, 0, 12, 13, 0, 0, 0], [3,4,5,7,8,10,12,13,0,0,0,0,0,0,0,0,0]),

    # ([0, 0, 0, -25503, 20486, -94356, 0, -20253, 80325, 0, 62558, -41932, -63525, 0, 0, 0], []),
    # ([0,0,0,0,-25503,20486,-94356,0,-20253,80325,0,62558,-41932,-63525,0,0,0,0,0,-16051,-896,0,-7783,0,0,-26335,19267,-33350,0,73475,0,82325,68084,-60140,0,78072,98839,0,0,-83121,0,-32293,16421,48223,0,-8846,73852,-48827,12788,-68476,0,0],[]),
)

def test():
    for q, (x, y) in enumerate(inputs):
        move_zeroes(x)
        print( x == y, (q, x, y))
test()

    return failed


if __name__ == "__main__":
    import sys
    sys.exit(test())

