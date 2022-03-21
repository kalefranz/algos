## implement bubble sort
## strategy: Compare two numbers n[0] and n[1], if number on left is larger than number on right, then swap().
##           Continue looping until end of array. When finished with one iteration, start again at beginning,
##           and this time stop at array.length-1. Operation will be O(n^2).

def run_tests(func):
    test_arrays = (
        [3,2,1],
        [3,1,7,34,44,4],
        [3,1,7,5,23,24],
        [],
        [1],
        [2,1],
        [5,4,3,2,1],
        [4,8,6,2,4,6,1,3]
    )
    for q, test_array in enumerate(test_arrays):
        tester = list(test_array)
        tester = func(tester)
        for i in range(len(tester)-1):
            assert tester[i] <= tester[i+1], (q, test_array, tester)
    print("[ok]", func.__name__)


def swap_in_place(arr, i, j):
    arr[j], arr[i] = arr[i], arr[j]


def bubble_sort(arr):
    for i in range(len(arr), 1, -1):
        for j in range(0, i-1):
            if arr[j] > arr[j+1]:
                swap_in_place(arr, j, j+1)
    return arr
run_tests(bubble_sort)


def bubble_sort_optimized(arr):
    for i in range(len(arr), 1, -1):
        did_swap = False
        for j in range(0, i-1):
            if arr[j] > arr[j+1]:
                did_swap = True
                swap_in_place(arr, j, j+1)
        if not did_swap:
            break
    return arr
run_tests(bubble_sort_optimized)


## implement selection sort
## strategy: The idea with selection sort is that you "select" the smallest value on each loop
#            through, and then move that smallest value to the front. After one pass through,
#            the next iteration starts at the second element of the array.
def selection_sort(arr):
    for i in range(0, len(arr)-1):
        smallest_idx = i
        for j in range(i, len(arr)-1):
            if arr[j+1] < arr[smallest_idx]:
                smallest_idx = j+1
        if smallest_idx != i:
            swap_in_place(arr, i, smallest_idx)
    return arr
run_tests(selection_sort)


## implement insertion sort
## strategy: Insertion sort uses a pivot point as it scans through the array, and the portion
##           of the array to the left of the pivot is guaranteed sorted. Easiest way to think
##           of insertion sort is that we have a stream of numbers coming in, and each time we
##           process a new number, we put it in the correct position. We do this by comparing
##           to the last item in the sorted portion, and swap indexes down until the number
##           is in the right position.
def insertion_sort(arr):
    for i in range(1, len(arr)):
        for j in range(i, 0, -1):
            if arr[j] < arr[j-1]:
                swap_in_place(arr, j, j-1)
            else:
                break
    return arr
run_tests(insertion_sort)


## implement merge sort
## strategy: Take two known-sorted arrays, and merge them together. Split larger arrays into smaller
##           arrays, until array size is one, then merge back up recursively.

def merge_arrays(arr1, arr2):
    if not arr1:
        return list(arr2)
    if not arr2:
        return list(arr1)
    merged = []
    q1 = q2 = 0
    while True:
        if arr1[q1] < arr2[q2]:
            merged.append(arr1[q1])
            if q1 == len(arr1)-1:
                # q1 was advanced 1 too far
                # use up arr2, then we're done
                merged.extend(arr2[q2:])
                break
            q1 += 1
        else:
            merged.append(arr2[q2])
            if q2 == len(arr2)-1:
                merged.extend(arr1[q1:])
                break
            q2 += 1
    return merged


def test_merge():
    assert merge_arrays([1,3,4], [2,7,8]) == [1,2,3,4,7,8], (merge_arrays([1,3,4], [2,7,8]), [1,2,3,4,7,8])
    assert merge_arrays([], []) == []
    assert merge_arrays([1], []) == [1]
    assert merge_arrays([], [3]) == [3]
    assert merge_arrays([1,2], []) == [1,2]
    assert merge_arrays([], [3,4]) == [3,4]
    assert merge_arrays([1,2], [3,4]) == [1,2,3,4]
test_merge()


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    merged = merge_arrays(merge_sort(arr[0:mid]), merge_sort(arr[mid:]))
    return merged
run_tests(merge_sort)



## implement quick sort
## strategy: Take the first element of the array, and then swap left any number that's less. Then split
##           array at final swap point, and recursively run the algo again.

def partition(arr):
    if len(arr) <= 1:
        return arr
    pivot = 1
    xval = arr[0]
    for i in range(1, len(arr)):
        if arr[i] < xval:
            swap_in_place(arr, i, pivot)
            pivot += 1
    swap_in_place(arr, 0, pivot-1)
    return arr[0:pivot], arr[pivot:]

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    arr1, arr2 = partition(arr)
    return quick_sort(arr1) + quick_sort(arr2)

run_tests(quick_sort)



# implement toposort
