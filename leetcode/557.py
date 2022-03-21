from typing import *

def reverseWords(s: str) -> str:
    builder = []
    stack = []
    for c in s:
        if c != ' ':
            stack.append(c)
        else:
            word = ''.join(reversed(stack))
            builder.append(word)
            stack.clear()
    word = ''.join(reversed(stack))
    builder.append(word)
    return ' '.join(builder)
