"""
19. Remove Nth Node From End of List
Medium

Given the head of a linked list, remove the nth node from the end of the list and return its head.


This file also contains ListNode constructor for testing purposes.

Biggest PoS problem I've ever experienced with leetcode.  Seriously wtf.


leetcode interals:
>>> import sys
>>> print(sys.path)
<<Nothing>>


>>> print(vars(ListNode))
{'__module__': 'precompiled.listnode', '__init__': <function ListNode.__init__ at 0x7f2938072050>, '__str__': <function ListNode.__str__ at 0x7f29380720e0>, '__repr__': <function ListNode.__repr__ at 0x7f2938072170>, '_array_to_list_node': <staticmethod(<function ListNode._array_to_list_node at 0x7f2938072200>)>, 'has_cycle': <staticmethod(<function ListNode.has_cycle at 0x7f2938072290>)>, 'deserialize': <staticmethod(<function ListNode.deserialize at 0x7f2938072320>)>, 'serialize': <classmethod(<function ListNode.serialize at 0x7f29380723b0>)>, '__dict__': <attribute '__dict__' of 'ListNode' objects>, '__weakref__': <attribute '__weakref__' of 'ListNode' objects>, '__doc__': None}
>> print(dir(ListNode))
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_array_to_list_node', 'deserialize', 'has_cycle', 'serialize']




>>> print("globals():", globals())
<< Nothing on globals() >>

>>> print("locals():", locals())
All Rights Reserved.

Copyright (c) 2000 BeOpen.com.
All Rights Reserved.

Copyright (c) 1995-2001 Corporation for National Research Initiatives.
All Rights Reserved.

Copyright (c) 1991-1995 Stichting Mathematisch Centrum, Amsterdam.
locals(): {
  'self': <__main__.Solution object at 0x7fccc00f3190>,
  'head': ListNode{val: 1, next: ListNode{val: 2, next: ListNode{val: 3, next: ListNode{val: 4, next: ListNode{val: 5, next: None}}}}},
  'n': 2,
  'sys': <module 'sys' (built-in)>
}


>>> import sys
>>> print(sys)
>>> print(vars(sys))
>>> print(dir(sys))
>>> print(type(sys))

>>> import sys
>>> print("sys =", sys)
>>> print("vars(sys) =", vars(sys))
>>> print("dir(sys) =", dir(sys))
>>> print("type(sys) =", type(sys))
sys = <module 'sys' (built-in)>
dir(sys) = [
  '__breakpointhook__', '__displayhook__', '__doc__', '__excepthook__', '__interactivehook__', '__loader__', '__name__',
  '__package__', '__spec__', '__stderr__', '__stdin__', '__stdout__', '__unraisablehook__', '_base_executable',
  '_clear_type_cache', '_current_exceptions', '_current_frames', '_deactivate_opcache', '_debugmallocstats',
  '_framework', '_getframe', '_git', '_home', '_xoptions', 'abiflags', 'addaudithook', 'api_version', 'argv', 'audit',
  'base_exec_prefix', 'base_prefix', 'breakpointhook', 'builtin_module_names', 'byteorder', 'call_tracing',
  'copyright', 'displayhook', 'dont_write_bytecode', 'exc_info', 'excepthook', 'exec_prefix', 'executable',
  'exit', 'flags', 'float_info', 'float_repr_style', 'get_asyncgen_hooks', 'get_coroutine_origin_tracking_depth',
  'getallocatedblocks', 'getdefaultencoding', 'getdlopenflags', 'getfilesystemencodeerrors',
  'getfilesystemencoding', 'getprofile', 'getrecursionlimit', 'getrefcount',
  'getsizeof', 'getswitchinterval', 'gettrace',...
]

type(sys) = <class 'module'>


# >>> print('>>>>>> <<<<<<<\n\n')
>>> import os
>>> print(f"env: {os.environ}")
>>> print("x", os.environ)
>>> print("d", dir(os))
>>> print("v", vars(os))
# >>> print('>>>>>> <<<<<<<\n\n')










# >>>>>> <<<<<<<

env: environ({'PATH': '/usr/local/bin:/usr/bin:/bin', 'LC_CTYPE': 'C.UTF-8'})
x environ({'PATH': '/usr/local/bin:/usr/bin:/bin', 'LC_CTYPE': 'C.UTF-8'})
d ['CLD_CONTINUED', 'CLD_DUMPED', 'CLD_EXITED', 'CLD_KILLED', 'CLD_STOPPED', 'CLD_TRAPPED', 'DirEntry', 'EFD_CLOEXEC',
   'EFD_NONBLOCK', 'EFD_SEMAPHORE', 'EX_CANTCREAT', 'EX_CONFIG', 'EX_DATAERR', 'EX_IOERR', 'EX_NOHOST', 'EX_NOINPUT',
   'EX_NOPERM', 'EX_NOUSER', 'EX_OK', 'EX_OSERR', 'EX_OSFILE', 'EX_PROTOCOL', 'EX_SOFTWARE', 'EX_TEMPFAIL',
   'EX_UNAVAILABLE', 'EX_USAGE', 'F_LOCK', 'F_OK', 'F_TEST', 'F_TLOCK', 'F_ULOCK', 'GRND_NONBLOCK', 'GRND_RANDOM',
   'GenericAlias', 'MFD_ALLOW_SEALING', 'MFD_CLOEXEC', 'MFD_HUGETLB', 'MFD_HUGE_16GB', 'MFD_HUGE_16MB', 'MFD_HUGE_1GB',
   'MFD_HUGE_1MB', 'MFD_HUGE_256MB', 'MFD_HUGE_2GB', 'MFD_HUGE_2MB', 'MFD_HUGE_32MB', 'MFD_HUGE_512KB', 'MFD_HUGE_512MB',
    'MFD_HUGE_64KB', 'MFD_HUGE_8MB', 'MFD_HUGE_MASK', 'MFD_HUGE_SHIFT', 'Mapping', 'MutableMapping', 'NGROUPS_MAX',
    'O_ACCMODE', 'O_APPEND', 'O_ASYNC', 'O_CLOEXEC', 'O_CREAT', 'O_DIRECT', 'O_DIRECTORY', 'O_DSYNC', 'O_EXCL',
    'O_FSYNC', 'O_LARGEFILE', 'O_NDELAY', 'O_NOATIME', 'O_NOCTTY', 'O_NOFOLLOW', 'O_NONBLOCK', 'O...
v {'__name__': 'os', '__doc__': "OS routines for NT or Posix depending on what system we're on.\n\nThis exports:\n  - all functions from posix or nt, e.g. unlink, stat, etc.\n  - os.path is either posixpath or ntpath\n  - os.name is either 'posix' or 'nt'\n  - os.curdir is a string representing the current directory (always '.')\n  - os.pardir is a string representing the parent directory (always '..')\n  - os.sep is the (or a most common) pathname separator ('/' or '\\\\')\n  - os.extsep is the extension separator (always '.')\n  - os.altsep is the alternate pathname separator (None or '/')\n  - os.pathsep is the component separator used in $PATH etc\n  - os.linesep is the line separator in text files ('\\r' or '\\n' or '\\r\\n')\n  - os.defpath is the default search path for executables\n  - os.devnull is the file path of the null device ('/dev/null', etc.)\n\nPrograms that import and use 'os' stand a better chance of being\nportable between different platforms.  Of course, they must...
All Rights Reserved.

Copyright (c) 2000 BeOpen.com.
All Rights Reserved.

Copyright (c) 1995-2001 Corporation for National Research Initiatives.
All Rights Reserved.

Copyright (c) 1991-1995 Stichting Mathematisch Centrum, Amsterdam.
All Rights Reserved., 'credits':     Thanks to CWI, CNRI, BeOpen.com, Zope Corporation and a cast of thousands
    for supporting Python development.  See www.python.org for more information., 'license': Type license() to see the full license text, 'help': Type help() for interactive help, or help(object) for help about object.}, 'abc': <module 'abc' from '/usr/lib/python3.10/abc.py'>, 'sys': <module 'sys' (built-in)>, 'st': <module 'stat' from '/usr/lib/python3.10/stat.py'>, '_check_methods': <function _check_methods at 0x7fdc0f271750>, 'GenericAlias': <class 'types.GenericAlias'>, '__all__': ['altsep', 'curdir', 'pardir', 'sep', 'pathsep', 'linesep', 'defpath', 'name', 'path', 'devnull', 'SEEK_SET', 'SEEK_CUR', 'SEEK_END', 'fsencode', 'fsdecode', 'get_exec_path', 'fdopen', 'extsep', '_exit', 'CLD_CONTINUED', 'CLD_DUMPED', 'CLD_EXITED', 'CLD_KILLED', 'CLD_STOPPED', 'CLD_TRAPPED', 'DirEntry', 'EFD_CLOEXEC', 'EFD_NONBLOCK', 'EFD_SEMAPHORE', 'EX_CANTCREAT', 'EX_CONFIG', 'EX_DATAERR', 'EX_IOERR', 'EX_NOHOST', 'EX_NOINPUT', 'EX_NOPERM', 'EX_NOUSER', 'EX_OK', 'EX_OSERR', 'EX_OSFILE', 'EX_PROTOCOL', ...
# >>>>>> <<<<<<<

from textwrap import TextWrapper
tw = TextWrapper(width=50)
[len(line) for line in tw.wrap(str(dir(os)))]

"""
import textwrap


import sys

textwrap

from collections import deque
from typing import *

import conda

# # ## Definition for singly-linked list.
class ListNode:
    """
    vars(): {'__module__': 'precompiled.listnode', '__init__': <function ListNode.__init__ at 0x7f82cc8c1fc0>, '__str__': <function ListNode.__str__ at 0x7f82cc8c2050>, '__repr__': <function ListNode.__repr__ at 0x7f82cc8c20e0>, '_array_to_list_node': <staticmethod(<function ListNode._array_to_list_node at 0x7f82cc8c2170>)>, 'has_cycle': <staticmethod(<function ListNode.has_cycle at 0x7f82cc8c2200>)>, 'deserialize': <staticmethod(<function ListNode.deserialize at 0x7f82cc8c2290>)>, 'serialize': <classmethod(<function ListNode.serialize at 0x7f82cc8c2320>)>, '__dict__': <attribute '__dict__' of 'ListNode' objects>, '__weakref__': <attribute '__weakref__' of 'ListNode' objects>, '__doc__': None}
    dir(): ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_array_to_list_node', 'deserialize', 'has_cycle', 'serialize']
    inspect.getsource()

    """
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"ListNode({self.val},{self.next})"

    def as_py_list(self):
        def itr():
            node = self
            while node:
                if node.val:
                    yield node.val
                node = node.next
        return list(itr())

    @classmethod
    def from_list(cls, lst):
        tail = None
        for v in reversed(lst):
            if tail is None:
                tail = node = cls(v)
            else:
                node = cls(v, node)
        head = node
        return head


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        hold = deque(maxlen=n+1)
        node = head
        hold.append(node)
        while node and node.next:
            node = node.next
            hold.append(node)
        if len(hold) <= 1 and n == 1:
            node.val = ''
            return node
        # if len(hold) <= 1 and n == 2:
        #     return ListNode(2)

        tail = node
        # assert len(hold) == n+1, len(hold)
        remove_head_side = hold.popleft()
        remove_node = hold.popleft()
        remove_tail_side = hold.popleft() if hold else None
        remove_head_side.next = remove_tail_side
        return head



TEST_CALL = Solution().removeNthFromEnd
CASES = (
    # ## expected, *input_args
    ([1,2,3,5], [1,2,3,4,5], 2),
    ([], [1], 1),
    ([1], [1,2], 1),
    ([2], [1,2], 2),
)
def test(*test_nums):
    cases = test_nums and [CASES[num] for num in test_nums] or CASES

    failed = 0
    for q, (expected, *input_args) in enumerate(cases):
        head = ListNode.from_list(input_args[0])
        result = TEST_CALL(head, input_args[1])
        result = result.as_py_list()
        if result == expected:
            print(f"{q}: passed")
        else:
            print(f"{q}: FAILED")
            print(f"  {expected} != {result}")
            failed += 1
    if failed:
        print(f"FAILED: {failed}")
    else:
        print(f"SUCCESS: TESTS PASSED == {len(cases)}")
test(3)
