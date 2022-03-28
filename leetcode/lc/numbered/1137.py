class Solution:
    _cache = [0, 1, 1]
    def tribonacci(self, n: int) -> int:
        _cache = self.__class__._cache
        for i in range(len(_cache), n+1):
            _cache.append(_cache[i-1] + _cache[i-2] + _cache[i-3])
        return _cache[n]

print(Solution().tribonacci(25))

    return failed


if __name__ == "__main__":
    import sys
    sys.exit(test())

