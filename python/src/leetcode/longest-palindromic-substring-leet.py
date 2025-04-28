#Given a string s, return the longest palindromic substring in s.


    # def is_palindrome_end_to_mid(self, s: str) -> bool:
    #     l: str = len(s)
    #     for i in range(0, l//2):
    #         if s[i] != s[l - 1 - i]:
    #             return False

    #     return True
# =================================
    # def is_palindrome(self, s: str) -> bool:
    #     # if s == '': return True
    #     l = len(s)
    #     mid = l // 2
    #     offset = 1 if l % 2 == 0 else 0
    #     for i in range(0, mid):
    #         if s[mid - i - offset] != s[mid + i]:
    #             return False

    #     return True

class Solution:

    def get_longest_palindrome_at_pos(self, s: str, mid_point: int, max_len: int, offset: int):
        i: int = 0
        start = end = mid_point
        while True:
            tmp_start = mid_point - i - offset
            tmp_end = mid_point + i
            if tmp_start < 0 or tmp_end > max_len - 1:
                break

            if s[tmp_start] == s[tmp_end]:
                start = tmp_start
                end = tmp_end
            else:
                break
            i += 1

        # the end interval is not included when slicing
        return s[start: end + 1]

    def longestPalindrome(self, s: str) -> str:
        current_max = ''
        l = len(s)
        for i in range(0, l):
            result = self.get_longest_palindrome_at_pos(s, i, l, 0)
            if len(result) > len(current_max):
                current_max = result

            result = self.get_longest_palindrome_at_pos(s, i, l, 1)
            if len(result) > len(current_max):
                current_max = result

        return current_max

if __name__ == '__main__':
    sol = Solution()


    def test_longest_palindrome(s):
        print(f'string: {s}')
        print(f'Max palindrome: {sol.longestPalindrome(s)}')
        print('------------------------------------------------------------------')

    test_longest_palindrome('ccd')
    test_longest_palindrome('b')
    test_longest_palindrome('bb')
    test_longest_palindrome('bbb')
    test_longest_palindrome('bbbb')
    test_longest_palindrome('babad')
    test_longest_palindrome('cbbd')
    test_longest_palindrome('cbbc')
    test_longest_palindrome('xabxdca')


    # result = sol.longestPalindrome('babad')
    # print(s)
    # assert s == 'bab' or s =='aba'

    # s = sol.longestPalindrome('cbbd')
    # print(s)
    # assert s == 'bb'

    # ---------

    def test_is_palindrome(s, is_palindrome):
        print(f'"{s}" is_palindrome: {is_palindrome}: {sol.is_palindrome(s)}')
        assert sol.is_palindrome(s) == is_palindrome

    # test_is_palindrome('', True)
    # test_is_palindrome('a', True)
    # test_is_palindrome('aa', True)
    # test_is_palindrome('ab', False)
    # test_is_palindrome('aba', True)
    # test_is_palindrome('abba', True)
    # test_is_palindrome('aabba', False)
    # test_is_palindrome('abf1ba', False)
