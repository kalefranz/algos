inputs = (
    # "a2b3[cz]d",
    # "3[a]2[bc]",
    # "3[a2[c]]",
    # "2[abc]3[cd]ef",
    # "abc3[cd]xyz",
    # "1[f1[g1[h]]]gh",
    # "3[z]2[2[y]pq4[2[jk]e1[f]]]ef",
    # "e1[f]",
    # "2a2a2a",
    # "2[a2ab]",
    # "2[2[y]pq]",
    # "a1b2c",
    "1a1b2[2y]pq",
)


# import re
# # regex = re.compile(r"([0-9]+\[|[0-9]+|[a-z]+|\])")
# regex = re.compile(r"([0-9]+|[a-z]+|\[|\])")
# for ss in inputs:
#     ggs = Groups()
#     tokens = tuple(match for match in regex.findall(ss))
#     for token in tokens:
#         ggs.add_token(token)
#     print("%r     %s" % (ggs, ggs))


def decode_string(s):
    stack = []
    for c in s:
        if c == "]":
            decoded = []
            while stack[-1] != "[":
                decoded.append(stack.pop())
            stack.pop()  # stack[q] == '['
            k = 0
            base = 1
            while stack and stack[-1].isdigit():
                k += int(stack.pop()) * base
                base *= 10
            while k != 0:
                for ss in reversed(decoded):
                    stack.append(ss)
                k -= 1
        else:
            stack.append(c)

    return ''.join(stack)

decode_string("3[a2[bc]]")
