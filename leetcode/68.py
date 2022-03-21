from typing import List
from pprint import pprint


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        def format_line(_bldr, _bldr_len):
            extra_spaces = maxWidth - _bldr_len
            total_spaces = len(_bldr) - 1 + extra_spaces
            if len(_bldr) > 1:
                each_space, num_words_padded = divmod(total_spaces, len(_bldr) - 1)
            else:
                each_space = extra_spaces
                num_words_padded = 0
            b2 = []
            for q, _wrd in enumerate(_bldr):
                b2.append(_wrd)
                if len(_bldr) == 1 or q < len(_bldr)-1:
                    b2.append(' ' * each_space)
                if q < num_words_padded:
                    b2.append(' ')
            return ''.join(b2)

        lines = []
        builder = [words[0]]
        builder_len = len(words[0])
        for word in words[1:]:
            if builder_len + 1 + len(word) > maxWidth:
                lines.append(format_line(builder, builder_len))
                builder = [word]
                builder_len = len(word)
            else:
                builder.append(word)
                builder_len += 1 + len(word)
        if builder:
            right_pad = maxWidth - builder_len
            lines.append(' '.join(builder) + ' '*right_pad)
        return lines

    def prnt(self, lines):
        strng = '\n'.join(f'"{x}"  [{len(x)}]' for x in lines)
        print(strng)
        print()
        return strng

s = Solution()

words = ["This", "is", "an", "example", "of", "text", "justification."]
s.prnt(s.fullJustify(words, 16))

words = ["What","must","be","acknowledgment","shall","be"]
s.prnt(s.fullJustify(words, 16))

words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"]
s.prnt(s.fullJustify(words, 20))

words = ["ask","not","what","your","country","can","do","for","you","ask","what","you","can","do","for","your","country"]
s.prnt(s.fullJustify(words, 16))

words = ["a"]
s.prnt(s.fullJustify(words, 2))
s.prnt(s.fullJustify(words, 3))
