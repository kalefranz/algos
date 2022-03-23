def isBadVersion(x):
    return x >= 2



def firstBadVersion(n):
    cache = {}
    def is_bad_version(x):
        if x not in cache:
            cache[x] = isBadVersion(x)
        return cache[x]

    left, right = 0, n
    while left < right:
        target = (right - left) // 2 + left
        t1 = is_bad_version(target)
        t2 = is_bad_version(target+1)
        if (t1, t2) == (False, True):
            return target + 1
        elif (t1, t2) == (False, False):
            left = target + 1
        else:
            right = target


print(firstBadVersion(2))
