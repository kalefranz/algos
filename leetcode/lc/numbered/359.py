"""
359. Logger Rate Limiter
Easy

Design a logger system that receives a stream of messages along with their timestamps. Each unique message should only be printed at most every 10 seconds (i.e. a message printed at timestamp t will prevent other identical messages from being printed until timestamp t + 10).

All messages will come in chronological order. Several messages may arrive at the same timestamp.

Implement the Logger class:

    Logger() Initializes the logger object.
    bool shouldPrintMessage(int timestamp, string message) Returns true if the message should be printed in the given timestamp, otherwise returns false.


"""
from collections import deque
from time import time
from typing import *


class Logger:

    def __init__(self):
        self.messages = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        # Each unique message should only be printed at most every 10 seconds
        old_timestamp = self.messages.get(message)
        if old_timestamp is None:
            self.messages[message] = timestamp
            return True
        elif timestamp - old_timestamp >= 10:
            self.messages[message] = timestamp
            return True
        else:
            return False


null, true, false = None, True, False
CASES = (
    (
        [null, true, true, false, false, false, true],
        ["Logger", "shouldPrintMessage", "shouldPrintMessage", "shouldPrintMessage", "shouldPrintMessage", "shouldPrintMessage", "shouldPrintMessage"],
        [[], [1, "foo"], [2, "bar"], [3, "foo"], [8, "bar"], [10, "foo"], [11, "foo"]],
    ),
)


def test(*test_nums):
    cases = test_nums and [CASES[num] for num in test_nums] or CASES

    failed = 0
    for q, case in enumerate(cases):
        for qq, (expected, func, args) in enumerate(zip(*case)):
            if qq == 0:
                instance = globals()[func](*args)
                instance_init = f"{func}{tuple(args)}"
                continue
            else:
                result = getattr(instance, func)(*args)
                if result == expected:
                    # print(f"{q}: passed")
                    pass
                else:
                    print(f"{q}/{qq}: FAILED  {instance_init}.{func}{tuple(args)}")
                    print(f"  {expected} != {result}")
                    failed += 1
                    break
    if failed:
        print(f"FAILED: {failed}")
    else:
        print(f"SUCCESS: TESTS PASSED == {len(cases)}")


test()
