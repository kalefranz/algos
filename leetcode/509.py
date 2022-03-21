class Solution:
    _cache = [0, 1]
    def fib(self, n: int) -> int:
        _cache = self.__class__._cache
        for i in range(len(_cache), n+1):
            _cache.append(_cache[i-1] + _cache[i-2])
        return _cache[n]

print(Solution().fib(6))
