"""
location: /leetcode/precompiled/nestedinteger.py
"""

import json


class NestedInteger(object):
    def __init__(self, value=None):
        self.setInteger(value)
        self._list = []

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return (
            "NestedInteger{_integer: "
            + str(self._integer)
            + ", _list: "
            + str(self._list)
            + "}"
        )

    def isInteger(self):
        return self._integer is not None

    def getInteger(self):
        return self._integer

    def setInteger(self, i):
        self._integer = i

    def getList(self):
        return self._list

    def add(self, ni):
        self._list.append(ni)
        self._integer = None

    @staticmethod
    def _token_to_nested_integer(token):
        root = NestedInteger()
        if isinstance(token, list):
            for i in range(0, len(token)):
                root.add(NestedInteger._token_to_nested_integer(token[i]))
        elif isinstance(token, int):
            root.setInteger(token)
        return root

    @staticmethod
    def deserialize(s):
        return NestedInteger._token_to_nested_integer(json.loads(s))

    @staticmethod
    def _serialize(nested_integer, serializer):
        if nested_integer.isInteger():
            return serializer._serialize(nested_integer.getInteger(), "integer")
        else:
            return serializer._serialize(
                nested_integer.getList(), "NestedInteger[]"
            )

    # TODO: depreciated. remove once new serializer has been deployed.
    @staticmethod
    def serialize(nested_integer, serializer):
        if nested_integer.isInteger():
            return serializer.serialize(nested_integer.getInteger())
        else:
            return serializer.serialize(nested_integer.getList())
