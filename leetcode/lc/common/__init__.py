import os
from .bitmask import BitMask

"""
## How to import module that starts with number ##

from importlib import import_module
p1905 = import_module("lc.numbered.1905")
test = p1905.test

"""


def cls():
    if os.getenv("PWD") is None:
        # cmd.exe or PS
        os.system('cls')
    else:
        # posix
        os.system('clear')


def pbcopy(text):
    import win32clipboard, win32con
    win32clipboard.OpenClipboard()
    try:
        win32clipboard.SetClipboardData(win32con.CF_UNICODETEXT, text)
    finally:
        win32clipboard.CloseClipboard()


def pbpaste():
    import win32clipboard, win32con
    win32clipboard.OpenClipboard()
    try:
        got = win32clipboard.GetClipboardData(win32con.CF_UNICODETEXT)
        return got
    finally:
        win32clipboard.CloseClipboard()
