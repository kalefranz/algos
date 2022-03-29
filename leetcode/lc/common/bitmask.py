"""
## Bit Manipulation Notes

https://web.archive.org/web/20220315051419/https://realpython.com/web/20220315051419/https://realpython.com/python-bitwise-operators/#bitmasks

>>> print(f"{42:b}")  # Print 42 in binary
101010
>>> print(f"{42:032b}")  # Print 42 in binary on 32 zero-padded digits
00000000000000000000000000101010
>>> bin(42)
'0b101010'
>>> age = 0b101010
>>> print(age)
42
>>> hex(42)
'0x2a'
>>> oct(42)
'0o52'
>>> 42 == 0b101010 == 0x2a == 0o52
True
>>> int("101010", 2)
42
>>> int("cafe", 16)
51966


### Bitmasks

>>> def get_bit(value, bit_index):
...     return value & (1 << bit_index)
...
>>> get_bit(0b10000000, bit_index=5)
0
>>> get_bit(0b10100000, bit_index=5)
32

>>> def get_normalized_bit(value, bit_index):
...     return (value >> bit_index) & 1
...
>>> get_normalized_bit(0b10000000, bit_index=5)
0
>>> get_normalized_bit(0b10100000, bit_index=5)
1

>>> def set_bit(value, bit_index):
...     return value | (1 << bit_index)
...
>>> set_bit(0b10000000, bit_index=5)
160
>>> bin(160)
'0b10100000'

>>> def clear_bit(value, bit_index):
...     return value & ~(1 << bit_index)
...
>>> clear_bit(0b11111111, bit_index=5)
223
>>> bin(223)
'0b11011111'

>>> def toggle_bit(value, bit_index):
...     return value ^ (1 << bit_index)
...
>>> x = 0b10100000
>>> for _ in range(5):
...     x = toggle_bit(x, bit_index=7)
...     print(bin(x))
...
0b100000
0b10100000
0b100000
0b10100000
0b100000


"""


class BitMask:
    def __init__(self, initial=0):
        self.store = initial

    def __int__(self):
        return self.store

    def __repr__(self):
        return f"{self.__class__.__name__}({self.store})"

    def __str__(self):
        return bin(self.store)

    def set_bit(self, bit_index):
        self.store = self.store | (1 << bit_index)
        return self.store

    def set_bit_strict(self, bit_index):
        if self.get_normalized_bit(bit_index):
            raise IndexError(bit_index, f"{bit_index} already set")
        return self.set_bit(bit_index)

    def toggle_bit(self, bit_index):
        self.store = self.store ^ (1 << bit_index)
        return self.store

    def clear_bit(self, bit_index):
        self.store = self.store & ~(1 << bit_index)
        return self.store

    def get_bit(self, bit_index):
        return self.store & (1 << bit_index)

    def get_normalized_bit(self, bit_index):
        return (self.store >> bit_index) & 1
