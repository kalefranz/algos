from typing import List




class Groups:
    def __init__(self) -> None:
        self.token_count = -1
        self.root = Group(0)
        self.root.count = 1
        self.stack = [self.root]
        self.prev_token = None

    def add_token(self, token):
        self.token_count += 1
        if not token:
            return self
        if self.token_count == 0:
            if token.isalpha():
                g = Group(1)
                g.suffix = token
                g.count = 1
                self.stack[-1].groups.append(g)
                self.stack.append(g)
            elif token.isdigit():
                g = Group(1)
                g.count = int(token)
                # self.stack[-1].groups.append(g)
                self.stack.append(g)
            else:
                raise NotImplementedError(token)
        else:
            if self.prev_token.isalpha():
                if token.isdigit():
                    # <<a>>
                    # new group, don't yet know if next token will be ] or alpha,
                    #   so don't yet know if new group should be adjacent or one level down
                    g1 = self.stack.pop()
                    g = Group(g1.num_parents)
                    g.count = int(token)
                    # self.stack[-1].groups.append(g)
                    self.stack.append(g)
                elif token == "[":
                    # new group at one level deeper
                    g1 = self.stack[-1]
                    assert 0

                elif token == "]":
                    print(token)
                    assert 0

                else:
                    raise NotImplementedError(token)
            elif self.prev_token.isdigit():
                if token.isalpha():
                    # <<b>>
                    # group at top of stack created in <<a>>
                    # this group needs to be adjacent to previous group in stack
                    g = self.stack.pop()
                    g.suffix = token
                    self.stack[-1].groups.append(g)
                    self.stack.append(g)
                elif token == "[":
                    # <<c>>
                    # group at top of stack created in <<a>>
                    # this group needs to be one level down
                    g = self.stack.pop()
                    g.num_parents += 1
                    # self.stack[-1].groups.append(g)
                    self.stack.append(g)
                elif token == "]":
                    print(token)
                    assert 0
                else:
                    raise NotImplementedError(token)
            elif self.prev_token == "[":
                if token.isalpha():
                    g = self.stack.pop()
                    g.suffix = token
                    self.stack.append(g)
                elif token.isdigit():
                    # make another one level deeper, like <<c>>
                    g1 = self.stack.pop()
                    g = Group(g1.num_parents+1)
                    g.count = int(token)
                    self.stack.append(g1)
                    g1.groups.append(g)
                    self.stack.append(g)

                else:
                    raise NotImplementedError(token)
            elif self.prev_token == "]":
                assert False

            else:
                raise NotImplementedError(token)



            # if token.isdigit():
            #     if self.prev_token.isalpha():
            #         g1 = self.stack[-1]
            #         g = Group(g1.num_parents)
            #         g.count = int(token)
            #         self.stack.append(g)
            #         self.root.groups.append(g)
            #     elif self.prev_token == "]":
            #         g1 = self.stack[-1]
            #         g = Group(g1.num_parents)
            #         g.count = int(token)
            #         self.stack.append(g)
            #         self.root.groups.append(g)
            #     elif self.prev_token == "[":
            #         g1 = self.stack[-1]
            #         g = Group(g1.num_parents+1)
            #         g.count = int(token)
            #         self.stack[-1].groups.append(g)
            #     else:
            #         raise NotImplementedError(token)
            # elif token.isalpha():
            #     if self.prev_token.isdigit():
            #         # add as suffix to prev group, close group
            #         g = self.stack[-1]
            #         g.suffix = token
            #     elif self.prev_token == "]":
            #         # add as suffix to prev group, close group
            #         g = self.stack[-1]
            #         g.suffix = token
            #     elif self.prev_token == "[":
            #         # start new subgroup of prev group, and add as suffix
            #         g = Group()
            #         g.count = 1
            #         g.suffix = token
            #         self.stack[-1].groups.append(g)
            #     else:
            #         raise NotImplementedError(token)
            # elif token == "[":
            #     # next token should be a new group
            #     g = self.stack[-1]
            # elif token == "]":
            #     # end of this node's groups
            #     g = self.stack.pop()
            # else:
            #     raise NotImplementedError(token)

        self.prev_group = g
        self.prev_token = token
        return self

    def __repr__(self) -> str:
        return ''.join(map(repr, self.root))

    def __str__(self) -> str:
        return ''.join(map(str, self.root))


class Group:

    # def __init__(self, num_parents: int, count: int = 1, suffix: str = '',) -> None:
    def __init__(self, num_parents: int) -> None:
        self.num_parents = num_parents
        self.count = 0
        self.groups: List[Group] = []
        self.suffix = ""

    def __str__(self):
        builder = []
        for _ in range(self.count):
            for group in self.groups:
                builder.append(f"{group}")
            builder.append(f"{self.suffix}")
        return ''.join(builder)

    def __repr__(self) -> str:
        builder = []
        if self.groups:
            group_repr = ''.join(map(repr, self.groups))
        else:
            group_repr = ''
        if self.count > 1:
            if group_repr:
                builder.append(f"{self.count}[{group_repr}]{self.suffix}")
            else:
                builder.append(f"{self.count}{self.suffix}")
        else:
            if self.suffix:
                if group_repr:
                    builder.append(f"[{group_repr}]{self.suffix}")
                else:
                    builder.append(f"{self.suffix}")
            else:
                builder.append(f"{group_repr}")
        return ''.join(map(str, builder))



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
import re
# regex = re.compile(r"([0-9]+\[|[0-9]+|[a-z]+|\])")
regex = re.compile(r"([0-9]+|[a-z]+|\[|\])")
for ss in inputs:
    ggs = Groups()
    tokens = tuple(match for match in regex.findall(ss))
    for token in tokens:
        ggs.add_token(token)
    print("%r     %s" % (ggs, ggs))

    return failed


if __name__ == "__main__":
    import sys
    sys.exit(test())

