import typing

class Solution:

    # O(n^2)
    def lengthOfLongestSubstring1(self, s: str) -> int:
        str_len = len(s)
        max_len = 0
        running_len = 0
        for i in range(0, str_len):
            if str_len - i < max(max_len, running_len):
                return max(max_len, running_len)
            visited_chars: typing.Set = set()
            running_len = 0
            for j in range(i, str_len):
                ch = s[j]
                if not ch in visited_chars:
                    running_len += 1
                    visited_chars.add(ch)
                else:
                    if max_len < running_len:
                        max_len = running_len
                    break
            if max_len < running_len:
                    max_len = running_len

        return max_len

        # O(n)
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        start: int = 0
        char_pos = {}
        for i in range(len(s)):
            ch = s[i]
            pos = char_pos.get(ch)
            if pos != None and pos >= start:
                # move the start index one position to the right in the str, because the current one
                # is duplicated and it is breaking the sequence
                start = pos + 1
            char_pos[ch] = i
            # arrays and lists are 0 based and we have at least 1 char seq for an array with a single element
            # that's why (+ 1)
            max_len = max(i - start + 1, max_len)

        return max_len

if __name__ == '__main__':
    # s = ''
    # s = 'abcabxcbb'
    # s = 'abcabcbb'
    # s = 'pwwkew'
    # s = 'bbbbb'
    # s = 'au'
    test_inputs = ['', 'abcabxcbb', 'abcabcbb', 'pwwkew', 'bbbbb', 'au']

    for inp in test_inputs:
        max_len = Solution().lengthOfLongestSubstring(inp)
        print(f'"{inp}", max_len = {max_len}')
        print('-----------------------------------')