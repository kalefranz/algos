"""
Extracted from "/leetcode/user_code/prog_joined.py"
for problem 944
https://leetcode.com/problems/rotting-oranges/

"""

# coding: utf-8
from string import *
from re import *
from datetime import *
from collections import *
from heapq import *
from bisect import *
from copy import *
from math import *
from random import *
from statistics import *
from itertools import *
from functools import *
from operator import *
from io import *
from sys import *
from json import *
from builtins import *

import string
import re
import datetime
import collections
import heapq
import bisect
import copy
import math
import random
import statistics
import itertools
import functools
import operator
import io
import sys
import json

import precompiled.__settings__
from precompiled.__deserializer__ import __Deserializer__
from precompiled.__deserializer__ import DeserializeError
from precompiled.__serializer__ import __Serializer__
from precompiled.__utils__ import __Utils__
from precompiled.listnode import ListNode
from precompiled.nestedinteger import NestedInteger
from precompiled.treenode import TreeNode

from typing import *

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


# user submitted code insert below
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # import traceback
        # traceback.print_stack()
        # print("\n".join(traceback.format_stack()))

        with open("/leetcode/user_code/prog_joined.py") as fh:
            print(fh.read())

        assert 1


import sys
import os
import ujson as json


def _driver():
    des = __Deserializer__()
    ser = __Serializer__()
    SEPARATOR = "\x1b\x09\x1d"
    f = open("user.out", "wb", 0)
    lines = __Utils__().read_lines()

    while True:
        line = next(lines, None)
        if line == None:
            break
        param_1 = des._deserialize(line, 'integer[][]')

        ret = Solution().orangesRotting(param_1)
        try:
            out = ser._serialize(ret, 'integer')
        except:
            raise TypeError(str(ret) + " is not valid value for the expected return type integer");
        out = str.encode(out + '\n')
        f.write(out)
        sys.stdout.write(SEPARATOR)


if __name__ == '__main__':
    _driver()
