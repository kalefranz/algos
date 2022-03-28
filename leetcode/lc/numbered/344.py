from typing import *


def reverseString(s: List[str]) -> None:
    def swap(i):
        b = len(s)-1-i
        s[b], s[i] = s[i], s[b]

    max = len(s) // 2
    if max == 0:
        return
    for q in range(max):
        swap(q)

    return failed


if __name__ == "__main__":
    import sys
    sys.exit(test())

